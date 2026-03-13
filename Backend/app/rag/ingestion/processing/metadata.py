# app/rag/ingestion/processing/metadata.py

from typing import List
from langchain_core.documents import Document

from app.rag.ingestion.processing.categorizer import detect_category
from app.rag.ingestion.processing.section_parser import extract_section_title


def enrich_metadata(documents: List[Document]) -> List[Document]:
    """
    Attach rich metadata to each chunk.
    """

    for i, doc in enumerate(documents):

        source_file = doc.metadata.get("source_file", "unknown")

        # Document name
        doc.metadata["document_name"] = source_file

        # Category
        doc.metadata["category"] = detect_category(source_file)

        # Section title
        doc.metadata["section_title"] = extract_section_title(
            doc.page_content
        )

        # Chunk position
        doc.metadata["chunk_index"] = i

        # Character length
        doc.metadata["char_length"] = len(doc.page_content)

        # Page number (if available from PDF loader)
        doc.metadata["page_number"] = doc.metadata.get("page", None)

    return documents