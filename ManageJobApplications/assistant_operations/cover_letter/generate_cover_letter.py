# ManageJobApplications/cover_letter/generate_cover_letter.py
from ManageAssistant.views.assistant.response_generator.response_generator import (
    generate_response, format_instruction_for_model
)
from ManageJobApplications.assistant_operations.cover_letter.instruction_for_model import cover_letter_instructions


def generate_cover_letter(client, user=None, application=None,
                          career_summary=None, resume=None, raw_cover_letter=None):
    """
    Generate an automated cover letter for the applicant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user (User): The user object containing user details.
    - application_description (str): The description of the job posting.
    - job_profile (str): User's job profile details.
    - resume (str): User's resume details.

    Returns:
    - automated_message (str): The generated automated message.
    """
    try:
        # Create instruction for generating the cover letter using the provided details
        extract_instructions = cover_letter_instructions(
            user=user,
            application=application,
            career_summary=career_summary,
            resume=resume
        )

        # Format the instruction for the model
        formatted_instruction = format_instruction_for_model(extract_instructions)

        # Generate the assistant response
        assistant_response = generate_response(
            formatted_instruction, client, temperature=0.1,
            max_tokens=4096, top_p=1.0, frequency_penalty=0.5,
            presence_penalty=0.5
        )

        # print(f'Cover Letter extraction request: {assistant_response}')
        # get_horizontal_line()

        return assistant_response

    except Exception as e:
        print("Error:", e)
        print("Assistant response generation failed. Please try again.")

        return None
