# ManageJobApplications/views/cover_letter/add_cover_letter/add_cover_letter/save_cover_letter.py
from django.core.exceptions import ValidationError
from ManageJobApplications.models import CoverLetter
from general_utils.error_logging import log_error


def save_cover_letter(application, user, valid_cover_letter_data):
    """
    Save a cover letter for the given application and user if the data is valid.

    Parameters:
    - application: The application to which the cover letter belongs.
    - user: The user who owns the cover letter.
    - valid_cover_letter_data: A dictionary containing the validated cover letter data.

    Returns:
    - The created CoverLetter object if successful, None otherwise.
    """
    if not valid_cover_letter_data:
        log_error("No valid cover letter data provided.")
        return None

    try:
        # Extract cover letter data with validation checks
        subject = valid_cover_letter_data.get('subject')
        assistant_observation = valid_cover_letter_data.get('assistant_observation')
        letter = valid_cover_letter_data.get('letter')

        if not subject or not letter:
            log_error(f"Incomplete cover letter data: {valid_cover_letter_data}")
            return None

        # Create the CoverLetter object
        cover_letter = CoverLetter.objects.create(
            application=application,
            user=user,
            subject=subject,
            assistant_observation=assistant_observation,
            letter=letter,
        )
        log_error(f"Cover letter created successfully for user {user} and application {application}")
        return cover_letter

    except ValidationError as e:
        log_error(f"Validation error while creating cover letter: {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error while creating cover letter: {str(e)}")

    return None
