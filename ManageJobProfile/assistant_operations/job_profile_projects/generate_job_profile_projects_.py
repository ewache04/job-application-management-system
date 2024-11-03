# ManageJobApplications/assistant_operations/job_profile_projects/generate_job_profile_projects_.py


def generate_job_profile_projects_(client, user, project_text):
    """
    Generate an automated message for the applicant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - job_description (str): The description of the job posting.

    Returns:
    - automated_message (str): The generated automated message.
    """

    from ManageAssistant.views.assistant.response_generator.response_generator import format_instruction_for_model, \
        generate_response
    from ManageJobProfile.assistant_operations.job_profile_projects.instruction_for_model import \
        job_profile_projects_instructions

    try:
        # Create instruction for translation using the job description
        extract_instructions = job_profile_projects_instructions(project_text, )

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
