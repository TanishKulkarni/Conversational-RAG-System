import re
from typing import Dict, List


def classify_query(question: str) -> Dict[str, object]:
    """
    Classify whether retrieval should focus on one policy type or multiple.
    Also infer simple metadata filters from user wording.
    """
    q = question.lower()
    policy_keywords = {
        "attendance": ["attendance", "absent", "leave"],
        "examination": ["exam", "examination", "revaluation", "backlog", "result"],
        "scholarship": ["scholarship", "financial aid", "fee waiver"],
        "disciplinary": ["disciplinary", "misconduct", "suspension", "ragging"],
        "hostel": ["hostel", "mess", "accommodation"],
        "fees": ["fee", "fees", "tuition", "payment", "refund"],
        "academic": ["registration", "credit", "cgpa", "course", "semester"],
    }

    matched_categories: List[str] = []
    for category, words in policy_keywords.items():
        if any(w in q for w in words):
            matched_categories.append(category)

    # Single category => targeted retrieval, multi/none => cross-document search.
    retrieval_type = "single_document" if len(matched_categories) == 1 else "cross_document"
    metadata_filter: Dict[str, object] = {}
    if len(matched_categories) == 1:
        metadata_filter["category"] = matched_categories[0]

    year_match = re.search(r"(20\d{2})", q)
    if year_match:
        metadata_filter["academic_year"] = year_match.group(1)

    # Very lightweight department extraction.
    department_aliases = {
        "cse": "computer science",
        "computer science": "computer science",
        "ai": "artificial intelligence",
        "ece": "electronics",
        "civil": "civil",
        "mechanical": "mechanical",
    }
    for token, normalized in department_aliases.items():
        if token in q:
            metadata_filter["department"] = normalized
            break

    return {
        "retrieval_type": retrieval_type,
        "metadata_filter": metadata_filter,
        "matched_categories": matched_categories,
    }
