from langchain_ollama import ChatOllama

def get_llm():
    """
    Load local LLM via Ollama.
    """
    llm = ChatOllama(
        model="mistral", # Change if needed
        temperature=0.2
    )

    return llm