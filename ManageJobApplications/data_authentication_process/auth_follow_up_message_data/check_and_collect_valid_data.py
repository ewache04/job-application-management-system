# ManageJobApplications/data_authentication_process/auth_follow_up_message_data/check_and_collect_valid_data.py
from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.auth_follow_up_message import \
    is_follow_up_message_data_valid
from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.auth_follow_up_message_subject import \
    is_follow_up_message_subject_data_valid


def check_and_collect_valid_data(follow_up_message_data):
    valid_data, invalid_data = {}, {}

    # Validate follow-up message subject
    if is_follow_up_message_subject_data_valid(follow_up_message_data):
        valid_data['follow_up_message_subject'] = follow_up_message_data.get('follow_up_message_subject')
    else:
        invalid_data['follow_up_message_subject'] = follow_up_message_data.get('follow_up_message_subject')

    # Validate follow-up message
    if is_follow_up_message_data_valid(follow_up_message_data):
        valid_data['follow_up_message'] = follow_up_message_data.get('follow_up_message')
    else:
        invalid_data['follow_up_message'] = follow_up_message_data.get('follow_up_message')

    return valid_data, invalid_data
