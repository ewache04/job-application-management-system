# ManageJobApplications/views/resume/add_resume/valid_resume_sample_data.py

def valid_resume_sample_data(user=None, application=None):
    """
    Generate sample data for a resume.

    Parameters:
    - user: Optional. User object containing user information.
    - application: Optional. Application object containing application details.

    Returns:
    - A dictionary containing sample resume data.
    """
    user_name = f"{user.first_name} {user.last_name}" if user else "John Doe"
    user_email = user.email if user else "john.doe@example.com"
    company_name = application.company_name if application else "a forward-thinking company"

    return {
        'resume_name': user_name,
        'resume_email': user_email,
        'resume_summary': (
            f'Experienced software developer with a strong background in developing scalable web '
            f'applications. Proficient in Python, Django, and React. Seeking to leverage expertise to '
            f'contribute to high-impact projects at {company_name}.'
        )
    }
