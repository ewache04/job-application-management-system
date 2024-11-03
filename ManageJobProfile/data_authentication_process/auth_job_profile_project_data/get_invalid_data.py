# ManageJobProfile/data_authentication_process/auth_job_profile_project_data/get_invalid_data.py

from ManageJobProfile.data_authentication_process.auth_job_profile_project_data.check_and_collect_valid_data import \
    check_and_collect_valid_data


def get_invalid_data(project_message_data):
    """
    Extract and return invalid data from the provided project message data.

    Parameters:
    - project_message_data (dict): The project message data to be checked.

    Returns:
    - dict: A dictionary containing the invalid project message data.
    """
    valid_data, invalid_data = check_and_collect_valid_data(project_message_data)
    return invalid_data
