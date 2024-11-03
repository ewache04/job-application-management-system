# ManageJobApplications/data_authentication_process/application_data/auth_resume_name.py

def is_resume_name_data_valid(resume_data):
    if 'resume_name' in resume_data:
        resume_name = resume_data.get('resume_name')
        if resume_name:
            return resume_name
        else:
            return None
    else:
        return None

