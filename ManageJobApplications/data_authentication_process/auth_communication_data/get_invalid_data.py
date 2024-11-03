# ManageJobApplications/data_authentication_process/auth_communication_data/get_invalid_data.py
from ManageJobApplications.data_authentication_process.auth_communication_data.check_and_collect_valid_data import (
    check_and_collect_valid_data
)


def get_invalid_data(communication_message_data):
    """
    Extract and return invalid data from the provided communication message data.

    Parameters:
    - communication_message_data (dict): The communication message data to be checked.

    Returns:
    - invalid_data (dict): A dictionary containing the invalid communication message data.
    """
    valid_data, invalid_data = check_and_collect_valid_data(communication_message_data)
    return invalid_data
