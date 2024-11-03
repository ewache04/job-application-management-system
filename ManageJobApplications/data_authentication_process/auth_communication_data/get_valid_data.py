from ManageJobApplications.data_authentication_process.auth_communication_data.check_and_collect_valid_data import \
    check_and_collect_valid_data
from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_communication_message_data_data(communication_message_data):
    valid_data, invalid_data = check_and_collect_valid_data(communication_message_data)

    print(f'Valid communication message Info: {valid_data.keys()}')
    get_horizontal_line()

    return valid_data
