# ManageJobApplications/data_authentication_process/auth_follow_up_message_data/auth_follow_up_message.py
def is_follow_up_message_data_valid(follow_up_message_data):
    if 'follow_up_message' in follow_up_message_data:
        follow_up_message = follow_up_message_data.get('follow_up_message')
        if follow_up_message:
            return follow_up_message
        else:
            return None
    else:
        return None
