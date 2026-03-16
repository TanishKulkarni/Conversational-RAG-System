
from app.rag.retrieval.retriever import get_retriever
from app.rag.generation.generator import generate_answer


def answer_query(query: str):

    retriever = get_retriever()

    # Retrieve relevant chunks
    docs = retriever.invoke(query)

    # Generate grounded answer
    answer = generate_answer(query, docs)

    return {
        "question": query,
        "answer": answer,
        "sources": [d.metadata for d in docs]
    }


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'exit'): ")

        if q.lower() == "exit":
            break

        result = answer_query(q)

        print("\nAnswer:\n", result["answer"])