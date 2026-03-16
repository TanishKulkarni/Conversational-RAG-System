from langchain_community.vectorstores import FAISS

def save_index(vector_store, path: str):
    """
    Persist FAISS index to disk
    """
    vector_store.save_local(path)

def load_index(path: str, embeddings):
    """
    Load existing FAISS index
    """
    return FAISS.load_local(
    path,
    embeddings,
    allow_dangerous_deserialization=True
)