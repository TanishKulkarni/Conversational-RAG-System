from app.rag.conversation.chat_handler import handle_chat
from app.rag.reliability.detector import is_no_answer_case
from app.rag.reliability.fallback import get_fallback_response
from app.rag.reliability.escalation import create_support_ticket
from app.rag.reliability.logger import log_failed_query

def safe_chat(session_id: str, message: str):
    result = handle_chat(session_id, message)

    docs = result.get("docs", [])
    docs_metadata = result.get("sources", [])

    # If no sources -> likely unknown query
    category = "general"
    applied_filter = result.get("applied_filter", {})
    if isinstance(applied_filter, dict):
        category = applied_filter.get("category", "general")

    answer_text = (result.get("answer") or "").lower()
    model_unsure = any(
        phrase in answer_text
        for phrase in [
            "do not know",
            "don't know",
            "not mentioned",
            "not provided in the context",
            "not available in the context",
        ]
    )

    if not docs_metadata or is_no_answer_case(docs) or model_unsure:
        log_failed_query(message)
        ticket = create_support_ticket(message)

        return {
            "answer": get_fallback_response(category),
            "escalation": {
                "ticket_id": ticket["ticket_id"],
                "message": "Your query has been forwarded for review."
            }
        }
    return result