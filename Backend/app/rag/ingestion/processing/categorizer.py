from langchain_core.documents import Document

def detect_category(source_file: str) -> str:
    """
    Infer policy category from filename.
    """
    name = source_file.lower()

    if "attendance" in name:
        return "attendance"
    elif "exam" in name:
        return "examination"
    elif "scholarship" in name:
        return "scholarship"
    elif "disciplinary" in name:
        return "disciplinary"
    elif "handbook" in name:
        return "academic"
    else:
        return "general"