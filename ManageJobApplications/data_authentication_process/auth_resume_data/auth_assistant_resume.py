# ManageJobApplications/data_authentication_process/application_data/auth_resume_email.py

def is_assistant_resume_data_valid(resume_data):
    if 'assistant_resume' in resume_data:
        assistant_resume = resume_data.get('assistant_resume')
        if assistant_resume:
            return assistant_resume
        else:
            return None
    else:
        return None
