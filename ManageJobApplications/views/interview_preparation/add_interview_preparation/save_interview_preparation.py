# ManageJobApplications/views/interview_preparation/add_interview_preparation/save_interview_preparation.py
from django.core.exceptions import ValidationError
from ManageJobApplications.models import InterviewPreparation
from general_utils.error_logging import log_error


def save_interview_preparation(application, user, valid_interview_preparation_data):
    """
    Save an interview preparation for the given application and user if the data is valid.

    Parameters:
    - application: The application to which the interview preparation belongs.
    - user: The user who owns the interview preparation.
    - valid_interview_preparation_data: A dictionary containing the validated interview preparation data.

    Returns:
    - The created InterviewPreparation object if successful, None otherwise.
    """
    if not valid_interview_preparation_data:
        log_error("No valid interview preparation data provided.")
        return None

    try:
        # Extract interview preparation data with validation checks
        about_company = valid_interview_preparation_data.get('about_company')
        prep_questions = valid_interview_preparation_data.get('prep_questions')

        # Debug logging to check the values being used to create the object
        print(f"About Company: {about_company}")
        print(f"Prep Questions: {prep_questions}")

        # Create the InterviewPreparation object
        interview_preparation = InterviewPreparation.objects.create(
            application=application,
            user=user,
            about_company=about_company,
            prep_questions=prep_questions
        )
        print(f"Interview Preparation created successfully for user {user} and application {application}")
        return interview_preparation

    except ValidationError as e:
        log_error(f"Validation error while creating interview preparation: {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error while creating interview preparation: {str(e)}")
    return None
