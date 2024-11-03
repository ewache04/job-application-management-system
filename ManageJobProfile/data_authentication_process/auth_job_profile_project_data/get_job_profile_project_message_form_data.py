# ManageJobApplications/data_authentication_process/auth_job_profile_project_data/get_job_profile_project_message_form_data.py

import time

from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import \
    parse_assistant_response
from ManageJobProfile.assistant_operations.job_profile_projects.generate_job_profile_projects_ import \
    generate_job_profile_projects_
from ManageJobProfile.data_authentication_process.auth_job_profile_project_data.get_valid_data import \
    get_valid_job_profile_project_message_data_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def get_job_profile_project_message_form_data(client, user, project_message_data):
    """
    Generate and parse the project message using the assistant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: The user object.
    - project_message_data (dict): The project message data to be processed.

    Returns:
    - dict: The valid project message form data, or None if unsuccessful.
    """
    retries = 0

    while retries < MAX_RETRIES:
        # Generate the project message using the assistant
        assistant_response = generate_job_profile_projects_(client, user, project_message_data)

        if assistant_response is None:
            print("Assistant response is None. Retry...")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)
            continue

        # Parse the assistant's response to extract the project message
        form_data = parse_assistant_response(assistant_response)

        if form_data is not None:
            # Convert the parsed response to form data
            form_data = convert_to_form_data(form_data)

            if form_data:
                form_data = get_valid_job_profile_project_message_data_data(form_data)
                return form_data
            else:
                print("Failed to convert parsed response to form data.")
                return None
        else:
            print(f"Failed to parse the assistant's response. Retry {retries + 1} of {MAX_RETRIES}.")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)

    print("Maximum number of retries exceeded. Unable to extract project message data.")
    return None
