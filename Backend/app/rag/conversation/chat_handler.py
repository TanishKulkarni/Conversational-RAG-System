from app.rag.retrieval.retriever import retrieve_documents
from app.rag.retrieval.query_classifier import classify_query
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

    classification = classify_query(standalone_query)
    retrieval_type = classification["retrieval_type"]
    metadata_filter = classification["metadata_filter"]
    top_k = 3 if retrieval_type == "single_document" else 6

    # Fallback to unfiltered retrieval if strict metadata filter yields no docs.
    docs = retrieve_documents(standalone_query, k=top_k, metadata_filter=metadata_filter)
    if not docs and metadata_filter:
        docs = retrieve_documents(standalone_query, k=top_k, metadata_filter=None)

    # Speed-first mode skips slow LLM generation and returns grounded snippet.
    speed_mode = os.getenv("SPEED_PRIORITY", "false").lower() == "true"
    answer = _fast_grounded_answer(docs) if speed_mode else generate_answer(standalone_query, docs)

    # Save interaction to memory
    memory.save_context(
        {"input": user_message},
        {"output": answer}
    )

    return {
        "question": user_message,
        "rewritten_query": standalone_query,
        "retrieval_type": retrieval_type,
        "applied_filter": metadata_filter,
        "answer": answer,
        "sources": [d.metadata for d in docs],
        "docs": docs
    }