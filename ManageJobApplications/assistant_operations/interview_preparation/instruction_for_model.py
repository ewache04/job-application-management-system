from ManageJobApplications.assistant_operations.interview_preparation.interview_prep_extraction_format import \
    interview_prep_extraction_structure


def interview_prep_instructions(user=None,
                                application=None,
                                career_summary=None,
                                raw_interview_preparation=None):
    """
    Generate structured instructions for extracting details for interview preparation.

    Parameters:
    - user: User object containing user information.
    - application: The application object containing job application details.
    - work_experience: Work experience related to the application.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """

    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    extraction_structure = interview_prep_extraction_structure()

    instruction_script = [
        {"role": "user", "content": "You are a professional interview preparation analyst."},
        {"role": "user", "content": "Study the data provided below."},
        {"role": "user", "content": f"Job posting details: {application}"},
        {"role": "user", "content": f"Applicant career summary: {career_summary}"},
        {"role": "user", "content": f"Raw interview preparation: {raw_interview_preparation}"},
        {"role": "user", "content": f"Applicant first name: {first_name}"},
        {"role": "user", "content": f"Applicant last name: {last_name}"},
        {"role": "user", "content": "Also study the extraction format below. Provide your response in list tuple "
                                    "format."},
        {"role": "user", "content": f"Extraction structure: {extraction_structure}"},
        {"role": "user", "content": (
            "Good format example: [('subject', 'my subject content goes here. (1,3,4,5,)')]. "
            "Bad format example: [('subject', 'my subject content goes here. [1,3,4,5,]')]. "
            "Avoid including this kind of error: SyntaxWarning: invalid escape sequence '\\', '\\S','\\U','\\D', "
            "'\\A', '\\B', '\\C', '\\E', '\\F', '\\G', '\\H', '\\I', '\\J', '\\K', '\\L', '\\N', '\\O', '\\P', '\\Q', "
            "'\\R', '\\T', '\\V', '\\W', '\\X', '\\Y', '\\Z'."
        )},
        {"role": "user", "content": (
            "When providing the 'about_company', include the following:\n"
            "- Overview of the company's history and mission.\n"
            "- Recent projects, developments, or achievements.\n"
            "- Key products or services offered by the company.\n"
            "- Information on company culture and values."
        )},
        {"role": "user", "content": (
            "When providing the 'prep_questions', ensure it includes:\n"
            "- Common interview questions for the role.\n"
            "- Behavioral questions to understand past experiences and skills.\n"
            "- Technical questions relevant to the job.\n"
            "- Any role-specific questions that align with the job description.\n"
            "Include 10 to 15 questions.\n"
            "Use the format: 1. Question.\n2. Question.\n3. Question."
        )},
        {"role": "user", "content": "Thanks! You may generate it now."},
        {"role": "assistant", "content": "Okay."},
    ]

    return instruction_script
