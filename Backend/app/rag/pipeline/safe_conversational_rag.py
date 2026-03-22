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
    if not docs_metadata or is_no_answer_case(docs):
        log_failed_query(message)
        ticket = create_support_ticket(message)

        return {
            "answer": get_fallback_response(),
            "escalation": {
                "ticket_id": ticket["ticket_id"],
                "message": "Your query has been forwarded for review."
            }
        }
    return result