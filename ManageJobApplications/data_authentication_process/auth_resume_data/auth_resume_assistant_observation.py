# ManageJobApplications/data_authentication_process/auth_resume_data/auth_resume_assistant_observation.py

def is_resume_assistant_observation_data_valid(resume_data):
    if 'assistant_observation' in resume_data:
        assistant_observation = resume_data.get('assistant_observation')
        if assistant_observation:
            return assistant_observation
        else:
            return None
    else:
        return None
