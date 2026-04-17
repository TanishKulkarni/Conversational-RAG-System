from app.rag.ingestion.embedding.embedder import get_embedding_model
from app.rag.ingestion.vectorstore.manager import load_index
from pathlib import Path
from functools import lru_cache

BASE_DIR = Path(__file__).resolve().parents[3]
VECTORSTORE_DIR = BASE_DIR / "data" / "vectorstore" / "faiss_index"

@lru_cache(maxsize=1)
def _get_cached_retriever():
    """
    Load FAISS index once and keep retriever cached in memory.
    """
    embeddings = get_embedding_model()
    vector_store = load_index(str(VECTORSTORE_DIR), embeddings)
    return vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )

def get_retriever(k: int = 3):
    """
    Get retriever with optional dynamic top-k override.
    """
    retriever = _get_cached_retriever()
    retriever.search_kwargs["k"] = k
    return retriever
