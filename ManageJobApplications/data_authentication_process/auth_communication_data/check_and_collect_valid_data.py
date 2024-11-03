# ManageJobApplications/data_authentication_process/auth_communication_data/check_and_collect_valid_data.py
from ManageJobApplications.data_authentication_process.auth_communication_data.auth_communication_subject import \
    is_communication_subject_data_valid
from ManageJobApplications.data_authentication_process.auth_communication_data.auth_communication_summary import \
    is_communication_summary_data_valid


def check_and_collect_valid_data(communication_message_data):
    valid_data, invalid_data = {}, {}

    # Validate communication subject
    if is_communication_subject_data_valid(communication_message_data):
        valid_data['communication_subject'] = communication_message_data.get('communication_subject')
    else:
        invalid_data['communication_subject'] = communication_message_data.get('communication_subject')

    # Validate communication summary
    if is_communication_summary_data_valid(communication_message_data):
        valid_data['communication_summary'] = communication_message_data.get('communication_summary')
    else:
        invalid_data['communication_summary'] = communication_message_data.get('communication_summary')

    return valid_data, invalid_data
