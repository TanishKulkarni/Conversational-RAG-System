def extract_section_title(text: str) -> str:
    """
    Extract probable section title from chunk text.
    Assumes headings appear at the start.
    """

    lines = text.strip().split("\n")

    for line in lines[:5]:  # check first few lines
        clean = line.strip()

        # Heuristic: short line, title case, no period
        if (
            5 < len(clean) < 120
            and clean.isupper() is False
            and clean.endswith(":")
        ):
            return clean.replace(":", "")

    return "Unknown Section"