import time

from ManageJobApplications.assistant_operations.resume.generate_resume import generate_resume
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import \
    parse_assistant_response
from ManageJobApplications.data_authentication_process.auth_resume_data.get_valid_data import get_valid_resume_data
from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def get_resume_form_data(client, user, application, work_experience=None, raw_resume=None):
    """
    Generate and parse the resume using the assistant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: The user object containing user information.
    - application: The job application object.
    - work_experience: The work experience details, optional.
    - raw_resume: The raw resume text, optional.

    Returns:
    - form_data (dict): The valid resume data, or None if unsuccessful.
    """
    retries = 0

    while retries < MAX_RETRIES:
        # Generate the resume using the assistant
        assistant_response = generate_resume(client, user, application, work_experience, raw_resume)

        # Parse the assistant's response to extract the resume
        form_data = parse_assistant_response(assistant_response)

        if form_data is not None:
            # Convert the parsed response to form data
            form_data = convert_to_form_data(form_data)

            if form_data:
                form_data = get_valid_resume_data(form_data)
                return form_data
            else:
                print("Failed to convert parsed response to form data.")
                return None
        else:
            print(f"Failed to parse the assistant's response. Retry {retries + 1} of {MAX_RETRIES}.")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)

    print("Maximum number of retries exceeded. Unable to extract resume data.")
    return None
