def get_fallback_response(category: str = "general"):
    contacts = {
        "attendance": "Attendance Cell (attendance@university.edu)",
        "examination": "Examination Office (exams@university.edu)",
        "scholarship": "Scholarship Desk (scholarships@university.edu)",
        "disciplinary": "Student Affairs Office (studentaffairs@university.edu)",
        "hostel": "Hostel Office (hostel@university.edu)",
        "fees": "Accounts Office (accounts@university.edu)",
        "academic": "Academic Office (academic@university.edu)",
        "general": "University Helpdesk (helpdesk@university.edu)",
    }
    contact = contacts.get(category, contacts["general"])
    return (
        "I could not find a confident policy answer from the indexed documents.\n\n"
        f"Please contact: {contact}\n"
        "You can also rephrase your question with policy name, year, and department."
    )