# ManageJobApplications/data_authentication_process/auth_job_profile_project_data/check_and_collect_valid_data.py
from ManageJobProfile.data_authentication_process.auth_job_profile_project_data.auth_project_subject import \
    is_project_subject_data_valid
from ManageJobProfile.data_authentication_process.auth_job_profile_project_data.auth_project_summary import \
    is_project_summary_data_valid


def check_and_collect_valid_data(project_message_data):
    valid_data, invalid_data = {}, {}

    # Validate project_subject
    if is_project_subject_data_valid(project_message_data):
        valid_data['project_subject'] = project_message_data.get('project_subject')
    else:
        invalid_data['project_subject'] = project_message_data.get('project_subject')

    # Validate project_summary
    if is_project_summary_data_valid(project_message_data):
        valid_data['project_summary'] = project_message_data.get('project_summary')
    else:
        invalid_data['project_summary'] = project_message_data.get('project_summary')

    return valid_data, invalid_data
