from django.db import IntegrityError
from ManageJobApplications.models import ApplicationProgressStatus
from general_utils.error_logging import log_error


def create_application_progress_status(application, user, interest_level=None, application_status=None):
    """
    Create an ApplicationProgressStatus for the given application and user with default values.

    Parameters:
    - application: The application to which the progress status belongs.
    - user: The user who owns the progress status.

    Returns:
    - The created ApplicationProgressStatus object if successful, None otherwise.
    """
    try:
        application_progress_status = ApplicationProgressStatus.objects.create(
            application=application,
            user=user,
            interest_level=interest_level or "Medium",  # Default interest level
            application_status=application_status or "Pending"  # Default application status
        )
        print('\nApplicationProgressStatus created successfully')
        return application_progress_status
    except IntegrityError as e:
        log_error(f"Integrity error while creating ApplicationProgressStatus: {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error while creating ApplicationProgressStatus: {str(e)}")

    return None
