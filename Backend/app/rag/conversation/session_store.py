from typing import Dict
from langchain_classic.memory import ConversationSummaryBufferMemory
from app.rag.conversation.memory import create_memory

# In-Memory session store(simple version)
sessions: Dict[str, ConversationSummaryBufferMemory] = {}

def get_session_memory(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = create_memory()

    return sessions[session_id]