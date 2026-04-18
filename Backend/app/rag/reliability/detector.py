from typing import List
from langchain_core.documents import Document

SIMILARITY_THRESHOLD = 1.2

def is_no_answer_case(docs: List[Document]) -> bool:
    """
    Determine whether retrieved context is insufficient.
    """
    if not docs:
        return True
    
    # Check similarity scores if available
    scores = [
        doc.metadata.get("score", 1.0)
        for doc in docs
        if "score" in doc.metadata
    ]

    # Lower score means closer match for FAISS L2 distance.
    if scores and min(scores) > SIMILARITY_THRESHOLD:
        return True
    
    # Check for extreme short text
    total_length = sum(len(d.page_content) for d in docs)

    if total_length < 200:
        return True
    
    return False

