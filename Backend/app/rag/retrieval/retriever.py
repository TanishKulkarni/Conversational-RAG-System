from app.rag.ingestion.embedding.embedder import get_embedding_model
from app.rag.ingestion.vectorstore.manager import load_index
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
VECTORSTORE_DIR = BASE_DIR / "data" / "vectorstore" / "faiss_index"

def get_retriever(k: int=4):
    """
    Load FAISS index and create retriever.
    """
    embeddings = get_embedding_model()
    vector_store = load_index(str(VECTORSTORE_DIR), embeddings)
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    return retriever
