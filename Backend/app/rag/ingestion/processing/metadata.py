from typing import List
from langchain_core.documents import Document

def enrich_metadata(documents: List[Document]) -> List[Document]:
    """
    Add useful metadata for retrieval and citation.
    """
    for doc in documents:
        # Estimate length
        doc.metadata["char_length"] = len(doc.page_content)

        # Identify policy category from filename
        source = doc.metadata.get("source_file", "").lower()

        if "attendance" in source:
            doc.metadata["category"] = "attendance"
        elif "exam" in source:
            doc.metadata["category"] = "examination"
        elif "scholarship" in source:
            doc.metadata["category"] = "scholarship"
        elif "disciplinary" in source:
            doc.metadata["category"] = "disciplinary"
        else:
            doc.metadata["category"] = "academic"

    return documents