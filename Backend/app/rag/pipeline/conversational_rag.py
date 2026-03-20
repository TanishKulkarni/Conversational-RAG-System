from app.rag.conversation.chat_handler import handle_chat

def chat(session_id: str, message: str):
    return handle_chat(session_id, message)