# ManageJobApplications/data_authentication_process/auth_communication_data/auth_communication_summary.py
def is_communication_summary_data_valid(communication_message_data):
    if 'communication_summary' in communication_message_data:
        communication_summary = communication_message_data.get('communication_summary')
        if communication_summary:
            return communication_summary
        else:
            return None
    else:
        return None
