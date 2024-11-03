# ManageJobApplications/cover_letter/instruction_for_model.py
from ManageJobApplications.assistant_operations.cover_letter.cover_letter_extraction_format import \
    cover_letter_extraction_structure


def cover_letter_instructions(user=None, application=None, career_summary=None, resume=None, raw_cover_letter=None):
    """
    Generate structured instructions for extracting details from a cover letter.

    Parameters:
    - user: User object containing user information.
    - application: The description of the job posting.
    - work_experience: User's work experience details.
    - resume: User's resume details.
    - raw_cover_letter: User's initial cover letter.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """
    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    extraction_structure = cover_letter_extraction_structure()

    instruction_script = [

        {"role": "user", "content": "You are a professional at writing cover letters for job applications."},
        {"role": "user", "content": (
            "I will provide you with the job description, my job profile, my resume, and possibly a raw cover letter. "
            "Please construct an amazing cover letter for me, addressing the hiring manager or recruiter, "
            "and expressing my interest in the position. Include relevant details from the job description and "
            "highlight how my experience aligns with the requirements. If the raw cover letter is relevant to the job "
            "description, use it as a base and update the information to match the job description, resume, "
            "job profile, and my user info. If the raw cover letter is not relevant, rewrite it to suit the job "
            "description I submitted."
        )},
        {"role": "user", "content": f"Job posting details: {application}"},
        {"role": "user", "content": f"Applicant Career summary: {career_summary}"},
        {"role": "user", "content": f"Uploaded resume details: {resume}"},
        {"role": "user", "content": f"Uploaded cover letter: {raw_cover_letter}"},
        {"role": "user", "content": f"Applicant first name: {first_name}"},
        {"role": "user", "content": f"Applicant last name: {last_name}"},
        {"role": "user", "content": (
            "Here is the exact format I wish for the assistant's response to be. Use square brackets as indicated. "
            "Anything other than this will break my program flow: "
            f"{extraction_structure}. "
            "Make the letter 1000-1440 tokens long. "
            "For listing items, use the format: (put items in here, e.g., 1,3,4,5). "
            "Do not include any decorative characters such as ** or \\n, as I will display it in the template. "
            "Good format example: [('subject','Enter the cover letter subject here. (1,3,4,5,)')]. "
            "Bad format example: [('subject','Enter the cover letter subject here. [1,3,4,5,]')]. "
            "Avoid including this kind of error: SyntaxWarning: invalid escape sequence '\\ ', '\\S','\\U','\\D',"
            "'\\T','\\L', '\\A', '\\B', '\\C', '\\E', '\\F', '\\G', '\\H', '\\I', '\\J', '\\K', '\\M', '\\N', '\\O',"
            "'\\P', '\\Q', '\\R', '\\V', '\\W', '\\X', '\\Y', '\\Z', '\\[', '\\]', '\\^', '\\_', '\\`', '\\a', '\\b',"
            "'\\c', '\\e', '\\f', '\\g', '\\h', '\\i', '\\j', '\\k', '\\l', '\\m', '\\o', '\\p', '\\q', '\\r', '\\s',"
            "'\\t', '\\u', '\\v', '\\w', '\\x', '\\y', '\\z'."
        )},
        {"role": "user", "content": (
            "If resume details, job profile, or first and last name are missing, be creative and generate a general "
            "cover letter using the provided information."
        )},
        {"role": "user", "content": (
            "Ensure the cover letter contains a well-crafted introduction, body, and conclusion. "
            "The introduction should express interest in the position and briefly mention relevant experience. "
            "The body should provide detailed examples of skills and achievements, tailored to the job description. "
            "The conclusion should reiterate interest, express gratitude, and provide contact information."
        )},
        {"role": "user", "content": (
            "When providing the 'assistant_observation', include an analysis of the cover letter's structure, content "
            "quality, strengths, weaknesses, and specific advice for improvement based on the job description and "
            "other provided details."
        )},
        {"role": "user", "content": "Thanks! You may generate it now."},
        {"role": "assistant", "content": "Okay."},
    ]

    return instruction_script
