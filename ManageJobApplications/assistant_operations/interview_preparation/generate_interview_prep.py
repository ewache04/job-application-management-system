from ManageAssistant.views.assistant.response_generator.response_generator import format_instruction_for_model, \
    generate_response
from ManageJobApplications.assistant_operations.interview_preparation.instruction_for_model import \
    interview_prep_instructions
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.get_valid_data import \
    get_valid_interview_prep_data


def generate_interview_prep(client, user,
                            application=None,
                            career_summary=None,
                            raw_interview_preparation=None):
    """
    Generate an automated message to extract details for interview preparation.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user (User): The user object containing user details.
    - application: The application object containing job application details.

    Returns:
    - automated_message (str): The generated automated message.
    """
    try:
        # Debugging: Print input parameters
        # print(f"User: {user}")
        # print(f"Application: {application}")
        # print(f"Work Experience: {work_experience}")

        # Create instruction for interview preparation extraction using the provided parameters
        extract_instructions = interview_prep_instructions(
            user=user,
            application=application,
            career_summary=career_summary,
            raw_interview_preparation=raw_interview_preparation,
        )

        # Format the instruction for the model
        formatted_instruction = format_instruction_for_model(extract_instructions)

        # Generate the assistant response
        assistant_response = generate_response(
            formatted_instruction, client, temperature=0.1,
            max_tokens=4096, top_p=1.0, frequency_penalty=0.5,
            presence_penalty=0.5
        )

        # Debugging: Print assistant response
        print(f"Assistant Response: {assistant_response}")
        return assistant_response

    except Exception as e:
        print("Error:", e)
        print(f"Assistant response generation failed. Please try again. {str(e)}")
        return None
