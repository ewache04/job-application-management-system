# ManageJobApplications/views/resume/add_resume/add_resume_auto/save_resume.py
from django.core.exceptions import ValidationError
from ManageJobApplications.models import Resume
from general_utils.error_logging import log_error


def save_resume(application, user, valid_resume_data):
    """
    Save a resume for the given application and user if the data is valid.

    Parameters:
    - application: The application to which the resume belongs.
    - user: The user who owns the resume.
    - valid_resume_data: A dictionary containing the validated resume data.

    Returns:
    - The created Resume object if successful, None otherwise.
    """
    if not valid_resume_data:
        log_error("No valid resume data provided.")
        return None

    try:
        # Extract resume data with validation checks
        resume_name = valid_resume_data.get('resume_name')
        resume_email = valid_resume_data.get('resume_email')
        assistant_observation = valid_resume_data.get('assistant_observation')
        assistant_resume = valid_resume_data.get('assistant_resume')

        # Create the Resume object
        resume = Resume.objects.create(

            application=application,
            user=user,
            resume_name=resume_name,
            resume_email=resume_email,
            assistant_observation=assistant_observation,
            assistant_resume=assistant_resume
        )

        log_error(f"Resume created successfully for user {user} and application {application}")
        return resume

    except ValidationError as e:
        log_error(f"Validation error while creating resume: {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error while creating resume: {str(e)}")

    return None
