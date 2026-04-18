from functools import lru_cache
from pathlib import Path
from typing import Dict, List

from langchain_core.documents import Document
from app.rag.ingestion.embedding.embedder import get_embedding_model
from app.rag.ingestion.vectorstore.manager import load_index

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


@lru_cache(maxsize=1)
def _get_cached_vectorstore():
    embeddings = get_embedding_model()
    return load_index(str(VECTORSTORE_DIR), embeddings)


def get_retriever(k: int = 3):
    """
    Get retriever with optional dynamic top-k override.
    """
    retriever = _get_cached_retriever()
    retriever.search_kwargs["k"] = k
    return retriever


def retrieve_documents(query: str, k: int = 4, metadata_filter: Dict[str, object] | None = None) -> List[Document]:
    """
    Retrieve documents with optional metadata filter.
    """
    vector_store = _get_cached_vectorstore()
    pairs = vector_store.similarity_search_with_score(query=query, k=k, filter=metadata_filter)
    docs: List[Document] = []
    for doc, score in pairs:
        doc.metadata["score"] = float(score)
        docs.append(doc)
    return docs
