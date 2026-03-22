from app.rag.retrieval.retriever import get_retriever
from app.rag.generation.generator import generate_answer
from app.rag.conversation.session_store import get_session_memory
from app.rag.conversation.rewritter import rewrite_query

def handle_chat(session_id: str, user_message: str):
    memory = get_session_memory(session_id)

    # Get conversation history
    history = memory.load_memory_variables({}).get("history", "")

    # Rewrite follow-up question
    standalone_query = rewrite_query(user_message, history)

    # Retrieve relevant docs
    retriever = get_retriever()
    docs = retriever.invoke(standalone_query)

    # Generate grounded answer
    answer = generate_answer(standalone_query, docs) 

    # Save interaction to memory
    memory.save_context(
        {"input": user_message},
        {"output": answer}
    )

    return {
        "question": user_message,
        "rewritten_query": standalone_query,
        "answer": answer,
        "sources": [d.metadata for d in docs],
        "docs": docs
    }