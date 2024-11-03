# ManageJobApplications/data_authentication_process/auth_job_profile_project_data/auth_project_subject.py
def is_project_subject_data_valid(project_message_data):
    if 'project_subject' in project_message_data:
        project_subject = project_message_data.get('project_subject')
        if project_subject:
            return project_subject
        else:
            return None
    else:
        return None
