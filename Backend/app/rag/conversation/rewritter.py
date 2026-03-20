from app.rag.generation.llm import get_llm

def rewrite_query(question: str, chat_history: str) -> str:
    """
    Convert follow-up question into a standalone query.
    """

    llm = get_llm()

    prompt = f"""
    Rewrite the user's question into a stndalone question
    using the conversation history.

    History:
    {chat_history}
    
    Follow-up question:
    {question}

    Standalone question:
    """
    response = llm.invoke(prompt)
        
    return response.content.strip()