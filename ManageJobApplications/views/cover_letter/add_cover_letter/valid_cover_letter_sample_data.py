# ManageJobApplications/views/resume/add_resume/valid_cover_letter_sample_data.py

def valid_cover_letter_sample_data(user=None, application=None):
    """
    Generate sample data for a cover letter.

    Parameters:
    - user: Optional. User object containing user information.
    - application: Optional. Application object containing application details.

    Returns:
    - A dictionary containing sample cover letter data.
    """
    user_name = f"{user.first_name} {user.last_name}" if user else "John Doe"
    company_name = application.company_name if application else "a forward-thinking company"

    return {
        'subject': f'Cover Letter for {user_name}',
        'letter': (
            f'{user_name} is an experienced software developer with a strong background in developing scalable web '
            f'applications. Proficient in Python, Django, and React. Seeking to leverage expertise to '
            f'contribute to high-impact projects at {company_name}.'
        )

    }
