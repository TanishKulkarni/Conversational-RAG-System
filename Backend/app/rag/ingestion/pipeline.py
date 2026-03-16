# app/rag/ingestion/pipeline.py

from pathlib import Path

from app.rag.ingestion.loaders.universal_loader import load_documents
from app.rag.ingestion.processing.chunker import chunk_documents
from app.rag.ingestion.processing.metadata import enrich_metadata
from app.rag.ingestion.embedding.embedder import get_embedding_model
from app.rag.ingestion.vectorstore.store import create_files_index
from app.rag.ingestion.vectorstore.manager import save_index



BASE_DIR = Path(__file__).resolve().parents[3]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
VECTORSTORE_DIR = BASE_DIR / "data" / "vectorstore" / "faiss_index"


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

def run_embedding_pipeline():
    
    documents = run_ingestion()

    print("Load embedding Model")
    embeddings = get_embedding_model()

    print("Creating FAISS index...")
    vector_store = create_files_index(documents, embeddings)

    print("Saving FAISS index to disk")
    VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

    save_index(vector_store, str(VECTORSTORE_DIR))

    print("\n Vector database created successfully")

    return vector_store


if __name__ == "__main__":
    run_embedding_pipeline()