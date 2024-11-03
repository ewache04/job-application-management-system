# ManageCareerSummary/assistant/career_summary/generate_career_summary.py

from ManageAssistant.views.assistant.response_generator.response_generator import (
    generate_response, format_instruction_for_model
)

from ManageCareerSummary.assistant.career_summary.instruction_for_model import career_summary_instructions


def generate_career_summary(client, user, job_profiles, projects):

    """
    Generate an automated message for the applicant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: User object containing user information.
    - career_summary (str): Existing career summary of the user.
    - job_profile (str): Job profile of the user.
    - project (str): User's project details.

    Returns:
    - automated_message (str): The generated automated message.
    """
    try:
        # Create instruction for translation using the job description
        extract_instructions = career_summary_instructions(user, job_profiles, projects)

        # Format instruction for the model
        formatted_instruction = format_instruction_for_model(extract_instructions)

        # Generate assistant response
        assistant_response = generate_response(
            formatted_instruction, client, temperature=0.2,
            max_tokens=4096, top_p=1.0, frequency_penalty=0.5,
            presence_penalty=0.5
        )

        return assistant_response

    except Exception as e:
        print("Error:", e)
        print("Assistant response does not support the pattern. Regenerating response...")

        return None
