# ManageJobApplications/follow_up_message/instruction_for_model.py
from django.http import request

from ManageJobApplications.assistant_operations.follow_up_message.follow_up_extraction_format import \
    follow_up_extraction_structure


def follow_up_message_instructions(user=None,
                                   application=None,
                                   career_summary=None,
                                   resume=None,
                                   last_follow_up_message=None,
                                   new_follow_up_message=None):
    """
    Generate structured instructions for extracting details from a follow-up message.

    Parameters:
    - user: User object containing user information.
    - application: The description of the job posting.
    - work_experience: User's job profile details.
    - resume: User's resume details.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """
    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    extraction_structure = follow_up_extraction_structure()

    instruction_script = [
        {"role": "user",
         "content": "You are tasked with crafting a professional follow-up message for job applications."},
        {"role": "user", "content": (
            "Your task is to create a clear and concise follow-up message, reminding the hiring manager about your "
            "application."
            "Ensure to include the company name, position title, and job ID if provided."
        )},
        {"role": "user", "content": f"Job posting details: {application}"},
        {"role": "user", "content": f"Applicant Career summary: {career_summary}"},
        {"role": "user", "content": f"Resume details: {resume}"},
        {"role": "user", "content": f"Applicant last follow-up-message sent: {last_follow_up_message}"},
        {"role": "user", "content": f"Applicant draft of "
                                    f"new follow-up-message that is to be sent: {new_follow_up_message}"},
        {"role": "user", "content": f"Applicant first name: {first_name}"},
        {"role": "user", "content": f"Applicant last name: {last_name}"},
        {"role": "user", "content": (
            "The format for the assistant's response must be exact. Add square brackets as indicated: "
            f"{extraction_structure}. "
            "Ensure the follow-up message falls within 1000 - 1440 tokens. "
            "For listing items, use the format: (put items in here, e.g., 1,3,4,5). "
            "Avoid decorative characters such as ** or \\n, as it will be displayed in the template. "
            "Use square brackets correctly, for example: [('subject','my subject content goes here. (1,3,4,5,)')]. "
            "Incorrect usage: [('subject','my subject content goes here. [1,3,4,5,]')]. "
            "Avoid errors like: SyntaxWarning: invalid escape sequence '\\ ', '\\S','\\U','\\D',"
            "'\\T','\\L', '\\A', '\\B', '\\C', '\\E', '\\F', '\\G', '\\H', '\\I', '\\J', '\\K', '\\M', '\\N', '\\O',"
            "'\\P', '\\Q', '\\R', '\\V', '\\W', '\\X', '\\Y', '\\Z', '\\[', '\\]', '\\^', '\\_', '\\`', '\\a', '\\b',"
            "'\\c', '\\e', '\\f', '\\g', '\\h', '\\i', '\\j', '\\k', '\\l', '\\m', '\\o', '\\p', '\\q', '\\r', '\\s',"
            "'\\t', '\\u', '\\v', '\\w', '\\x', '\\y', '\\z'."
        )},
        {"role": "user", "content": (
            "If any resume details, job profile, first or last name is missing, "
            "create a general follow-up message using available information."
        )},
        {"role": "user", "content": "Thank you! You may proceed with generating it."},
        {"role": "assistant", "content": "Understood."},
    ]

    return instruction_script

# Example usage:
# print(follow_up_message_instructions())
