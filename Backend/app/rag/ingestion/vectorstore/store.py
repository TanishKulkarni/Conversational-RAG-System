from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from typing import List

def create_files_index(documents: List[Document], embeddings):
    """
    Create FAISS vector index from documents.
    """
    vector_store = FAISS.from_documents(documents, embeddings)

    return vector_store
