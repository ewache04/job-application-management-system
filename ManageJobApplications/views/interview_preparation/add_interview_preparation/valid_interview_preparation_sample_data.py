# ManageJobApplications/views/interview_preparation/add_interview_preparation/valid_interview_preparation_sample_data.py

def valid_interview_preparation_sample_data(user=None, application=None):
    """
    Generate sample data for interview preparation.

    Parameters:
    - user: Optional. User object containing user information.
    - application: Optional. Application object containing application details.

    Returns:
    - A dictionary containing sample interview preparation data.
    """
    user_name = f"{user.first_name} {user.last_name}" if user else "John Doe"
    company_name = application.company_name if application else "a forward-thinking company"

    return {
        'about_company': (
            f'{company_name} is a leading innovator in the tech industry, known for its cutting-edge products and '
            f'services. The company values creativity, teamwork, and excellence in all its endeavors.'
        ),
        'prep_questions': (
            '1. What are your strengths and weaknesses?\n'
            '2. Why do you want to work at this company?\n'
            '3. Describe a challenging project you worked on and how you overcame the challenges.'
        )
    }
