import time

from ManageJobApplications.assistant_operations.cover_letter.generate_cover_letter import generate_cover_letter
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import \
    parse_assistant_response

from ManageJobApplications.data_authentication_process.auth_cover_letter_data.get_valid_data import \
    get_valid_cover_letter_data
from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def get_cover_letter_form_data(client,
                               user=None,
                               application=None,
                               work_experience=None,
                               resume=None,
                               raw_cover_letter=None):
    """
    Generate and parse the cover letter using the assistant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: The user object containing user information.
    - application_description (str): The description of the job posting.

    Returns:
    - form_data (dict): The valid cover letter data, or None if unsuccessful.
    """
    retries = 0

    while retries < MAX_RETRIES:
        # Generate the cover letter using the assistant
        assistant_response = generate_cover_letter(client,
                                                   user,
                                                   application,
                                                   work_experience,
                                                   resume, raw_cover_letter)

        if assistant_response is None:
            print("Assistant response is None. Retry...")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)
            continue

        # Parse the assistant's response to extract the cover letter
        form_data = parse_assistant_response(assistant_response)

        if form_data is not None:
            # Convert the parsed response to form data
            form_data = convert_to_form_data(form_data)

            if form_data:
                form_data = get_valid_cover_letter_data(form_data)
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
