# ManageJobApplications/data_authentication_process/auth_resume_data/check_and_collect_valid_data.py
from ManageJobApplications.data_authentication_process.auth_resume_data.auth_assistant_resume import \
    is_assistant_resume_data_valid
from ManageJobApplications.data_authentication_process.auth_resume_data.auth_resume_assistant_observation import \
    is_resume_assistant_observation_data_valid
from ManageJobApplications.data_authentication_process.auth_resume_data.auth_resume_email import \
    is_resume_email_data_valid
from ManageJobApplications.data_authentication_process.auth_resume_data.auth_resume_name import \
    is_resume_name_data_valid


# Function to check and collect valid data
def check_and_collect_valid_data(resume_data):
    valid_data, invalid_data = {}, {}

    # Validate resume name
    if is_resume_name_data_valid(resume_data):
        valid_data['resume_name'] = resume_data.get('resume_name')
    else:
        invalid_data['resume_name'] = resume_data.get('resume_name')

    # Validate resume email
    if is_resume_email_data_valid(resume_data):
        valid_data['resume_email'] = resume_data.get('resume_email')
    else:
        invalid_data['resume_email'] = resume_data.get('resume_email')

    # Validate assistant resume
    if is_assistant_resume_data_valid(resume_data):
        valid_data['assistant_resume'] = resume_data.get('assistant_resume')
    else:
        invalid_data['assistant_resume'] = resume_data.get('assistant_resume')

    # Validate assistant observation
    if is_resume_assistant_observation_data_valid(resume_data):
        valid_data['assistant_observation'] = resume_data.get('assistant_observation')
    else:
        invalid_data['assistant_observation'] = resume_data.get('assistant_observation')

    return valid_data, invalid_data
