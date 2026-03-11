# app/rag/ingestion/loaders/universal_loader.py

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from app.rag.ingestion.loaders.text_loader import load_text_file


def load_documents(directory: str) -> List[Document]:
    """
    Load all supported documents from a directory.
    Supports: PDF, TXT
    """
    all_docs = []

    for file_path in Path(directory).rglob("*"):

        if file_path.suffix.lower() == ".pdf":
            print("Loading PDF:", file_path)

            loader = PyPDFLoader(str(file_path))
            docs = loader.load()

            for doc in docs:
                doc.metadata["source_file"] = file_path.name
                doc.metadata["file_type"] = "pdf"

            all_docs.extend(docs)

        elif file_path.suffix.lower() == ".txt":
            print("Loading TXT:", file_path)

            docs = load_text_file(str(file_path))
            all_docs.extend(docs)

    return all_docs