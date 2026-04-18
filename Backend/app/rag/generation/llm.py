from functools import lru_cache
import os
from langchain_groq import ChatGroq

@lru_cache(maxsize=1)
def get_llm():
    """
    Load Groq LLM for cloud deployment.
    """
    model_name = os.getenv("GROQ_MODEL", "llama3-8b-8192")
    api_key = os.getenv("GROQ_API_KEY")
    temperature = float(os.getenv("GROQ_TEMPERATURE", "0.2"))

    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is required")

    llm = ChatGroq(
        model=model_name,
        api_key=api_key,
        temperature=temperature,
    )

    return llm