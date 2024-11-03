# ManageJobApplications/data_authentication_process/auth_interview_preparation_data/get_valid_interview_prep_data.py
import time

from ManageJobApplications.assistant_operations.interview_preparation.generate_interview_prep import \
    generate_interview_prep
from ManageJobApplications.data_authentication_process.application_data.data_extraction_process.parse_assistant_response import \
    parse_assistant_response
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.get_valid_data import \
    get_valid_interview_prep_data
from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2


def get_interview_prep_form_data(client, user, application=None,
                                 work_experience=None, raw_interview_preparation=None):
    """
    Generate and parse the interview preparation using the assistant.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: The user object containing user information.
    - application: The application object containing job application details.

    Returns:
    - form_data (dict): The valid interview preparation data, or None if unsuccessful.
    """
    retries = 0

    while retries < MAX_RETRIES:
        try:
            # Generate the interview preparation using the assistant
            print(f"Generating interview preparation. Retry {retries + 1} of {MAX_RETRIES}.")

            assistant_response = generate_interview_prep(client, user,
                                                         application,
                                                         work_experience,
                                                         raw_interview_preparation)

            # Debugging: Print assistant response
            print(f"Assistant Response: {assistant_response}")

            if assistant_response is None:
                print("Assistant response is None. Retry...")
                retries += 1
                time.sleep(RETRY_DELAY_SECONDS)
                continue

            # Parse the assistant's response to extract the interview preparation
            print("Parsing assistant response...")
            form_data = parse_assistant_response(assistant_response)

            if form_data is not None:
                print(f"Parsed form data: {form_data}")

                # Convert the parsed response to form data
                form_data = convert_to_form_data(form_data)

                if form_data:
                    print(f"Converted form data: {form_data}")

                    # Validate the form data
                    valid_form_data = get_valid_interview_prep_data(form_data)

                    if valid_form_data:
                        print("Valid interview preparation data extracted successfully.")
                        return valid_form_data
                    else:
                        print("Failed to validate interview preparation data.")
                        return None
                else:
                    print("Failed to convert parsed response to form data.")
                    return None
            else:
                print(f"Failed to parse the assistant's response. Retry {retries + 1} of {MAX_RETRIES}.")
                retries += 1
                time.sleep(RETRY_DELAY_SECONDS)
        except Exception as e:
            print(f"An error occurred during interview preparation extraction: {str(e)}")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)

    print("Maximum number of retries exceeded. Unable to extract interview preparation data.")
    return None
