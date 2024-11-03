# ManageJobApplications/data_authentication_process/auth_resume_data/auth_resume_key_words_found.py
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.check_and_collect_valid_data import \
    check_and_collect_valid_data


def get_invalid_data(interview_preparation_data):
    """
    Extract and return invalid data from the provided interview preparation data.

    Parameters:
    - interview_preparation_data (dict): The interview preparation data to be checked.

    Returns:
    - invalid_data (dict): A dictionary containing the invalid interview preparation data.
    """
    valid_data, invalid_data = check_and_collect_valid_data(interview_preparation_data)
    return invalid_data
