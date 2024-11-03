from datetime import datetime
import time

from ManageJobApplications.data_authentication_process.application_data.data_collection_process.extract_application_data_process import \
    extract_application_data_process

from ManageJobApplications.utils.convert_to_form_data import convert_to_form_data

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 3


def extract_application_data(application_description, client, retries=0):
    """
    Extract application data with retry mechanism.

    Parameters:
    - application_description (str): The description of the job posting.
    - client: The client object for communicating with the assistant.
    - retries (int): Number of retries attempted.

    Returns:
    - application_data (dict): A dictionary containing the extracted application details, or None if unsuccessful.
    """
    while retries < MAX_RETRIES:
        form_data = extract_application_data_process(application_description, client)

        form_data = convert_to_form_data(form_data)

        print(f"\nCurrent Attempt: {retries + 1} of {MAX_RETRIES}")

        if form_data is not None:
            print(f'Data extraction process status: Passed!')
            return form_data
        else:
            print("\n\nExtracting process ongoing....")
            retries += 1
            time.sleep(RETRY_DELAY_SECONDS)

    print("Maximum number of retries exceeded. Unable to extract application data.")
    return None
