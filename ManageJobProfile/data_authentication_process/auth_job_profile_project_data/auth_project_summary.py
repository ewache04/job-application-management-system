# ManageJobApplications/data_authentication_process/auth_communication_data/auth_communication_summary.py
def is_project_summary_data_valid(project_message_data):
    if 'project_summary' in project_message_data:
        project_summary = project_message_data.get('project_summary')
        if project_summary:
            return project_summary
        else:
            return None
    else:
        return None
