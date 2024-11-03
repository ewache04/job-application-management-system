def interview_prep_extraction_structure():
    """
    Define the expected structure for extracting interview preparation details.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected interview preparation structure.
    """
    structure = [
        ('title', "Use content provided and provide a title for the interview preparation here. 20 - 30 characters. "
                  "If not found, enter 'None'."),
        ('about_company', "Provide an overview of the company here."),
        ('prep_questions', "Provide interview questions for preparation here. Format each question-answer pair as "
                           "follows:\n"
                           "1. Question.\n"
                           "2. Question.\n"
                           "Include 15 to 20 questions.")
    ]

    return structure


# Example usage:
# print(interview_prep_extraction_structure())
