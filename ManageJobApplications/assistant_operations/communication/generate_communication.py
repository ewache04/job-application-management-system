from ManageAssistant.views.assistant.response_generator.response_generator import (
    generate_response, format_instruction_for_model
)
from ManageJobApplications.assistant_operations.communication.instruction_for_model import communication_instructions


def generate_communication(client, user, company_message, applicant_message):
    """
    Generate an automated message for the applicant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - job_description (str): The description of the job posting.

    Returns:
    - automated_message (str): The generated automated message.
    """
    try:
        # Create instruction for translation using the job description
        extract_instructions = communication_instructions(user,
                                                          company_message,
                                                          applicant_message)

        # Format instruction for the model
        formatted_instruction = format_instruction_for_model(extract_instructions)

        # Generate assistant response
        assistant_response = generate_response(
            formatted_instruction, client, temperature=0.2,
            max_tokens=4096, top_p=1.0, frequency_penalty=0.5,
            presence_penalty=0.5
        )

        # print(f'Assistant response: {assistant_response}')
        # get_horizontal_line()

        return assistant_response

    except Exception as e:
        print("Error:", e)
        print("Assistant response does not support the pattern. Regenerating response...")

        return None
