from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.check_and_collect_valid_data import \
    check_and_collect_valid_data
from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_follow_up_message_data_data(follow_up_message_data):
    valid_data, invalid_data = check_and_collect_valid_data(follow_up_message_data)

    print(f'Valid follow up message Info: {valid_data.keys()}')
    get_horizontal_line()

    return valid_data

