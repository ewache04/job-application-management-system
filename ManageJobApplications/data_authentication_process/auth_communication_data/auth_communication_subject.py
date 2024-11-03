# ManageJobApplications/data_authentication_process/auth_communication_data/auth_follow_up_message.py
def is_communication_subject_data_valid(communication_message_data):
    if 'communication_subject' in communication_message_data:
        communication_subject = communication_message_data.get('communication_subject')
        if communication_subject:
            return communication_subject
        else:
            return None
    else:
        return None
