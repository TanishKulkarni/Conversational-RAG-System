import uuid
from app.rag.conversation.session_store import sessions

def create_session():
    sid = str(uuid.uuid4())
    return {"session_id": sid}

def get_session_history(session_id: str):

    memory = sessions.get(session_id)

    if not memory:
        return {"history": []}
    
    return memory.load_memory_variables([])

def delete_session(session_id: str):

    sessions.pop(session_id, None)

    return {"status": "deleted"}