from app.rag.pipeline.safe_conversational_rag import safe_chat

def process_chat(session_id: str, message: str):

    result = safe_chat(session_id, message)

    confidence = 0.9 if "sources" in result else 0.2

    return {
        "answer": result.get("answer"),
        "citations": result.get("sources", []),
        "confidence": confidence,
        "escalation": result.get("escalation")
    }