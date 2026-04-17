from functools import lru_cache
import os
from langchain_ollama import ChatOllama

@lru_cache(maxsize=1)
def get_llm():
    """
    Load local LLM via Ollama.
    """
    model_name = os.getenv("OLLAMA_MODEL", "llama2")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    num_predict = int(os.getenv("OLLAMA_NUM_PREDICT", "96"))
    num_ctx = int(os.getenv("OLLAMA_NUM_CTX", "1024"))
    llm = ChatOllama(
        model=model_name,
        base_url=base_url,
        temperature=0.2,
        num_predict=num_predict,
        num_ctx=num_ctx,
    )

    return llm