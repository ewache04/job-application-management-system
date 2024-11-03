# ManageJobApplications/data_authentication_process/auth_interview_preparation_data/auth_interview_prep_about_company.py
def is_about_company_data_valid(interview_preparation_data):
    if 'about_company' in interview_preparation_data:
        about_company = interview_preparation_data.get('about_company')
        if about_company and about_company.strip():
            return about_company
    return None


