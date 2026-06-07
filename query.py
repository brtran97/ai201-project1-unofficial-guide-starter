import os
from dotenv import load_dotenv
from groq import Groq
from embed import retrieve

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = (
    "You are a helpful UC Davis dining guide assistant. "
    "Answer the user's question using ONLY the information in the provided documents below. "
    "Do NOT use any outside knowledge. "
    "If the documents do not contain enough information to answer the question, "
    "say 'I don't have enough information on that.' "
    "Cite which source document(s) your answer draws from in your response."
)


def ask(question, k=5):
    results = retrieve(question, k=k)

    context = "\n\n".join(
        f"[Source: {r['source']}]\n{r['text']}" for r in results
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Documents:\n{context}\n\nQuestion: {question}"},
        ],
        temperature=0.3,
    )

    answer = response.choices[0].message.content
    sources = list(dict.fromkeys(r["source"] for r in results))

    return {"answer": answer, "sources": sources}


if __name__ == "__main__":
    result = ask("What is Aggie Cash and how does it work?")
    print("Answer:", result["answer"])
    print("\nSources:", result["sources"])
