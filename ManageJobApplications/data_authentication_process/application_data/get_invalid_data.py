from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.check_and_collect_valid_data import \
    check_and_collect_valid_data


def get_invalid_data(application_data):
    valid_data, invalid_data = check_and_collect_valid_data(application_data)
    return invalid_data
