# ManageJobApplications/data_authentication_process/auth_interview_preparation_data/auth_interview_prep_title.py
def is_title_data_valid(interview_preparation_data):
    if 'title' in interview_preparation_data:
        title = interview_preparation_data.get('title')
        if title and title.strip():
            return title
    return None

