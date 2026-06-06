import os
import glob
import re
import random


def load_documents(documents_dir="documents"):
    documents = []
    for filepath in sorted(glob.glob(os.path.join(documents_dir, "*.txt"))):
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        if text.strip():
            documents.append({"source": filename, "text": text})
    return documents


def clean_text(text):
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            bp = text.rfind(". ", start, end)
            if bp == -1 or bp <= start:
                bp = text.rfind(" ", start, end)
            if bp > start + overlap:
                end = bp + 1
        chunk = text[start:end].strip()
        if len(chunk) >= 20:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = max(start + 1, end - overlap)
    return chunks


def ingest(documents_dir="documents"):
    documents = load_documents(documents_dir)
    all_chunks = []
    for doc in documents:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "source": doc["source"],
                "chunk_index": i,
            })
    return all_chunks


if __name__ == "__main__":
    chunks = ingest()
    print(f"Documents loaded: {len(set(c['source'] for c in chunks))}")
    print(f"Total chunks: {len(chunks)}")
    print()

    samples = random.sample(chunks, min(5, len(chunks)))
    for i, chunk in enumerate(samples, 1):
        print(f"--- Sample {i} [source: {chunk['source']}, chunk: {chunk['chunk_index']}] ---")
        print(chunk["text"])
        print()
