# ManageJobApplications/data_authentication_process/auth_resume_data/auth_resume_key_words_found.py
from ManageJobApplications.data_authentication_process.auth_cover_letter_data.check_and_collect_valid_data import \
    check_and_collect_valid_data


def get_invalid_data(cover_letter_data):
    """
    Extract and return invalid data from the provided cover letter data.

    Parameters:
    - cover_letter_data (dict): The cover letter data to be checked.

    Returns:
    - invalid_data (dict): A dictionary containing the invalid cover letter data.
    """
    valid_data, invalid_data = check_and_collect_valid_data(cover_letter_data)
    return invalid_data
