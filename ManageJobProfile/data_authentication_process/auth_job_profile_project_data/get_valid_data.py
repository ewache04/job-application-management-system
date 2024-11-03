# ManageJobApplications/data_authentication_process/auth_job_profile_project_data/get_valid_data.py

from ManageJobProfile.data_authentication_process.auth_job_profile_project_data.check_and_collect_valid_data import \
    check_and_collect_valid_data
from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_job_profile_project_message_data(project_message_data):
    """
    Extract and return valid job profile project message data.

    Parameters:
    - project_message_data (dict): The project message data to be checked.

    Returns:
    - dict: A dictionary containing the valid project message data.
    """
    valid_data, invalid_data = check_and_collect_valid_data(project_message_data)

    print(f'Valid job project Info: {list(valid_data.keys())}')
    get_horizontal_line()

    return valid_data
