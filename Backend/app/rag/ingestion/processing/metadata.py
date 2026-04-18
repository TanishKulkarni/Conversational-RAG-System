# app/rag/ingestion/processing/metadata.py

from typing import List
import re
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

        # Academic year, e.g., "2024" from filename/content
        match = re.search(r"(20\d{2})", source_file) or re.search(r"(20\d{2})", doc.page_content[:300])
        doc.metadata["academic_year"] = match.group(1) if match else "unknown"

        # Lightweight department tagging by text hints
        text = doc.page_content.lower()
        if "computer science" in text or " cse " in f" {text} ":
            department = "computer science"
        elif "artificial intelligence" in text or " ai " in f" {text} ":
            department = "artificial intelligence"
        elif "electronics" in text or " ece " in f" {text} ":
            department = "electronics"
        elif "civil" in text:
            department = "civil"
        elif "mechanical" in text:
            department = "mechanical"
        else:
            department = "all"
        doc.metadata["department"] = department

    return documents