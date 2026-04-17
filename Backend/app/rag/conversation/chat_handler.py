from app.rag.retrieval.retriever import get_retriever
from app.rag.generation.generator import generate_answer
from app.rag.conversation.session_store import get_session_memory
import os

def _fast_grounded_answer(docs):
    if not docs:
        return "I could not find a matching policy in the indexed documents."
    best = docs[0]
    snippet = (best.page_content or "").strip().replace("\n", " ")
    snippet = snippet[:450]
    return f"{snippet}"

def handle_chat(session_id: str, user_message: str):
    memory = get_session_memory(session_id)

    # Get conversation history
    history = memory.load_memory_variables({}).get("history", "")

    # Use the raw user query for speed (skips rewrite LLM call).
    standalone_query = user_message

    # Retrieve relevant docs
    retriever = get_retriever()
    docs = retriever.invoke(standalone_query)

    # Speed-first mode skips slow LLM generation and returns grounded snippet.
    speed_mode = os.getenv("SPEED_PRIORITY", "true").lower() == "true"
    answer = _fast_grounded_answer(docs) if speed_mode else generate_answer(standalone_query, docs)

    # Save interaction to memory
    memory.save_context(
        {"input": user_message},
        {"output": answer}
    )

    return {
        "question": user_message,
        "rewritten_query": standalone_query,
        "answer": answer,
        "sources": [d.metadata for d in docs],
        "docs": docs
    }