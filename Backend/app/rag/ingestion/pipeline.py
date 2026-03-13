# app/rag/ingestion/pipeline.py

from pathlib import Path

from app.rag.ingestion.loaders.universal_loader import load_documents
from app.rag.ingestion.processing.chunker import chunk_documents
from app.rag.ingestion.processing.metadata import enrich_metadata


BASE_DIR = Path(__file__).resolve().parents[3]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


def run_ingestion():

    print("Loading documents from:", RAW_DATA_DIR)

    documents = load_documents(str(RAW_DATA_DIR))
    print(f"Loaded {len(documents)} raw documents.")

    # Step 3 — Chunking
    chunked_docs = chunk_documents(documents)
    print(f"Created {len(chunked_docs)} chunks.")

    # Step 4 — Metadata Enrichment
    enriched_docs = enrich_metadata(chunked_docs)

    # Preview
    if enriched_docs:
        print("\nSample chunk:")
        print(enriched_docs[0].page_content)
        print("\nMetadata:", enriched_docs[0].metadata)

    return enriched_docs


if __name__ == "__main__":
    run_ingestion()