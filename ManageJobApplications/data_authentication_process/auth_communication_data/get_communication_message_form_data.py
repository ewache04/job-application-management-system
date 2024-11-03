# ManageJobApplications/data_authentication_process/auth_communication_data/get_communication_message_form_data.py
from ManageJobApplications.assistant_operations.communication.generate_communication import generate_communication
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import \
    parse_assistant_response
from ManageJobApplications.data_authentication_process.auth_communication_data.get_valid_data import \
    get_valid_communication_message_data_data

import time

from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def get_communication_message_form_data(client, user, company_message, applicant_message):
    """
    Generate and parse the communication message using the assistant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - company_message (str): The message from the company.
    - applicant_message (str): The message from the applicant.

    Returns:
    - form_data (dict): The valid communication message data, or None if unsuccessful.
    """
    retries = 0

    while retries < MAX_RETRIES:
        # Generate the communication message using the assistant
        assistant_response = generate_communication(client, user, company_message, applicant_message)

        if assistant_response is None:
            print("Assistant response is None. Retry...")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)
            continue

        # Parse the assistant's response to extract the communication message
        form_data = parse_assistant_response(assistant_response)

        if form_data is not None:
            # Convert the parsed response to form data
            form_data = convert_to_form_data(form_data)

            if form_data:
                form_data = get_valid_communication_message_data_data(form_data)
                return form_data

            else:
                print("Failed to convert parsed response to form data.")
                return None
        else:
            print(f"Failed to parse the assistant's response. Retry {retries + 1} of {MAX_RETRIES}.")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)

    print("Maximum number of retries exceeded. Unable to extract communication data.")
    return None
