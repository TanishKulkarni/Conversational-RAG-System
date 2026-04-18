import uuid
from datetime import datetime

def create_support_ticket(question: str):
    ticket_id = str(uuid.uuid4())[:8]

    ticket = {
        "ticket_id": ticket_id,
        "question": question,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }

    return ticket