from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.check_and_collect_valid_data import (
    check_and_collect_valid_data
)


def get_invalid_data(follow_up_message_data):
    """
    Extract and return invalid data from the provided follow-up message data.

    Parameters:
    - follow_up_message_data (dict): The follow-up message data to be checked.

    Returns:
    - invalid_data (dict): A dictionary containing the invalid follow-up message data.
    """
    valid_data, invalid_data = check_and_collect_valid_data(follow_up_message_data)
    return invalid_data
