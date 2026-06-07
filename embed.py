import chromadb
from sentence_transformers import SentenceTransformer
from ingest import ingest

COLLECTION_NAME = "ucd_dining"
PERSIST_DIR = "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")


def build_vector_store():
    chunks = ingest()
    client = chromadb.PersistentClient(path=PERSIST_DIR)

    if COLLECTION_NAME in [c.name for c in client.list_collections()]:
        client.delete_collection(COLLECTION_NAME)
    collection = client.get_or_create_collection(
        COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )

    texts = [c["text"] for c in chunks]
    ids = [f"{c['source']}_{c['chunk_index']}" for c in chunks]
    metadatas = [{"source": c["source"], "chunk_index": c["chunk_index"]} for c in chunks]

    embeddings = model.encode(texts, show_progress_bar=True).tolist()

    batch_size = 100
    for i in range(0, len(ids), batch_size):
        end = i + batch_size
        collection.add(
            ids=ids[i:end],
            embeddings=embeddings[i:end],
            documents=texts[i:end],
            metadatas=metadatas[i:end],
        )

    print(f"Stored {collection.count()} chunks in ChromaDB")
    return collection


def retrieve(query, k=5):
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    collection = client.get_collection(COLLECTION_NAME)
    query_embedding = model.encode([query]).tolist()

    results = collection.query(query_embeddings=query_embedding, n_results=k)

    output = []
    for i in range(len(results["ids"][0])):
        output.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "chunk_index": results["metadatas"][0][i]["chunk_index"],
            "distance": results["distances"][0][i],
        })
    return output


if __name__ == "__main__":
    collection = build_vector_store()

    test_queries = [
        "Which dining locations accept meal plans?",
        "What is Aggie Cash and how does it work?",
        "At Gunrock cafe are there TVs available for watch parties?",
    ]

    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"QUERY: {query}")
        print("=" * 60)
        results = retrieve(query)
        for j, r in enumerate(results, 1):
            print(f"\n  [{j}] source: {r['source']} | chunk: {r['chunk_index']} | distance: {r['distance']:.4f}")
            print(f"      {r['text'][:200]}...")
