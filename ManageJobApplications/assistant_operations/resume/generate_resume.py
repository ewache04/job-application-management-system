# ManageJobApplications/resume/generate_resume.py
from ManageAssistant.views.assistant.response_generator.response_generator import (
    generate_response, format_instruction_for_model
)
from ManageJobApplications.assistant_operations.resume.instruction_for_model import resume_instructions


def generate_resume(client, user, application=None, career_summary=None,
                    raw_resume=None, ):
    """
    Generate an automated message to extract details from the user's resume.

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
        # Create instruction for resume extraction using the provided parameters
        extract_instructions = resume_instructions(
            user=user,
            application=application,
            career_summary=career_summary,
            raw_resume=raw_resume
        )

        # Format the instruction for the model
        formatted_instruction = format_instruction_for_model(extract_instructions)

        # Generate the assistant response
        assistant_response = generate_response(
            formatted_instruction, client, temperature=0.1,
            max_tokens=4096, top_p=1.0, frequency_penalty=1.0,
            presence_penalty=0.0
        )

        # print(f'Resume extraction request: {assistant_response}')
        # get_horizontal_line()

        return assistant_response

    except Exception as e:
        print("Error:", e)
        print("Assistant response generation failed. Please try again.")

        return None
