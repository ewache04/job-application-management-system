from ManageAssistant.views.assistant.response_generator.response_generator import (
    format_instruction_for_model, generate_response
)
from ManageJobApplications.assistant_operations.applications.instruction_for_model import (
    job_description_extraction_instructions
)
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import (
    parse_assistant_response
)


def extract_application_data_process(application_description, client):
    """
    Extract application data from the assistant's response.

    Parameters:
    - application_description (str): The description of the job posting.
    - client: The client object for communicating with the assistant.

    Returns:
    - application_data (dict): A dictionary containing the extracted application details.
    """
    try:
        # Create instruction for translation using the selected target language(s)
        extract_instructions = job_description_extraction_instructions(application_description)

        # Format instruction for the model
        formatted_instruction = format_instruction_for_model(extract_instructions)

        # Generate assistant response
        assistant_response = generate_response(
            formatted_instruction, client, temperature=0.0,
            max_tokens=4096, top_p=0.1, frequency_penalty=0.5,
            presence_penalty=0.5
        )

        # Parse assistant response and extract application details
        application_data = parse_assistant_response(assistant_response)

        return application_data

    except Exception as e:
        print("Error:", e)
        print("Assistant response does not support the pattern. Regenerating response...")

        return None
