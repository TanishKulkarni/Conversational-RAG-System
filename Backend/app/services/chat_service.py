from app.rag.pipeline.safe_conversational_rag import safe_chat
from time import perf_counter

def process_chat(session_id: str, message: str):
    start = perf_counter()
    result = safe_chat(session_id, message)
    latency_ms = round((perf_counter() - start) * 1000, 2)

    confidence = 0.9 if "sources" in result else 0.2

    return {
        "answer": result.get("answer"),
        "citations": result.get("sources", []),
        "confidence": confidence,
        "escalation": result.get("escalation"),
        "retrieval_type": result.get("retrieval_type"),
        "applied_filter": result.get("applied_filter"),
        "latency_ms": latency_ms,
    }