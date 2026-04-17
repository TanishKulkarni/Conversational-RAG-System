from langchain_classic.memory import ConversationBufferMemory

def create_memory():
    """
    Create lightweight memory for a conversation session.
    """
    memory = ConversationBufferMemory(
        return_messages=False
    )

    return memory