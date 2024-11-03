# ManageJobApplications/data_authentication_process/application_data/auth_resume_email.py

def is_resume_email_data_valid(resume_data):
    if 'resume_email' in resume_data:
        resume_email = resume_data.get('resume_email')
        if resume_email:
            return resume_email
        else:
            return None
    else:
        return None
