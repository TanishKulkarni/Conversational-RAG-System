from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    Load open-source embedding model (BGE Large)
    """
    model_name = 'BAAI/bge-large-en-v1.5'

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"}, #Change to "cuda" for GPU(will see later)
        encode_kwargs={"normalize_embeddings": True}
    )

    return embeddings