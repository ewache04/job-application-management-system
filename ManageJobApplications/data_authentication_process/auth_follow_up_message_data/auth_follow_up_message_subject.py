# ManageJobApplications/data_authentication_process/auth_follow_up_message_data/auth_follow_up_message_subject.py
def is_follow_up_message_subject_data_valid(follow_up_message_data):
    if 'follow_up_message_subject' in follow_up_message_data:
        follow_up_message_subject = follow_up_message_data.get('follow_up_message_subject')
        if follow_up_message_subject:
            return follow_up_message_subject
        else:
            return None
    else:
        return None
