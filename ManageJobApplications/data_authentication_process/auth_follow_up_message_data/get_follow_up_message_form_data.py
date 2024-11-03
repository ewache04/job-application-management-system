from ManageJobApplications.assistant_operations.follow_up_message.generate_follow_up_message import \
    generate_follow_up_message
from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.get_valid_data import \
    get_valid_follow_up_message_data_data
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import \
    parse_assistant_response

import time

from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def get_follow_up_message_form_data(client,
                                    user,
                                    application,
                                    work_experience=None,
                                    resume=None,
                                    last_follow_up_message=None,
                                    new_follow_up_message=None):
    """
    Generate and parse the follow-up message using the assistant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: The user object containing user information.
    - application_description (str): The description of the job posting.

    Returns:
    - form_data (dict): The valid follow-up message data, or None if unsuccessful.
    """
    retries = 0

    while retries < MAX_RETRIES:
        # Generate the follow-up message using the assistant
        assistant_response = generate_follow_up_message(client,
                                                        user,
                                                        application,
                                                        work_experience,
                                                        resume,
                                                        last_follow_up_message,
                                                        new_follow_up_message)

        if assistant_response is None:
            print("Assistant response is None. Retry...")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)
            continue

        # Parse the assistant's response to extract the follow-up message
        form_data = parse_assistant_response(assistant_response)

        if form_data is not None:
            # Convert the parsed response to form data
            form_data = convert_to_form_data(form_data)

            if form_data:
                form_data = get_valid_follow_up_message_data_data(form_data)
                return form_data

            else:
                print("Failed to convert parsed response to form data.")
                return None
        else:
            print(f"Failed to parse the assistant's response. Retry {retries + 1} of {MAX_RETRIES}.")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)

    print("Maximum number of retries exceeded. Unable to extract application data.")
    return None
