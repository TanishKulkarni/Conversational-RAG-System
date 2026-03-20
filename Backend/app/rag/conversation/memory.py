from langchain_classic.memory import ConversationSummaryBufferMemory
from app.rag.generation.llm import get_llm

def create_memory():
    """
    Create summarizing memory for a conversation session.
    """

    memory = ConversationSummaryBufferMemory(
        llm=get_llm(),
        max_token_limit=2000,
        return_messages=True
    )

    return memory