# ManageJobApplications/urls/progress_status_urlpatterns.py
from django.urls import path


def get_progress_status_urlpatterns():
    """
    Retrieve URL patterns for progress status management.

    This function defines URL patterns for managing the progress status of job applications.

    Returns:
        list: A list of URL patterns for progress status management.
    """
    # Import necessary module
    from ManageJobApplications.views.application_progress_status.update_application_progress_status import \
        update_application_progress_status

    # Define URL patterns
    progress_status_urlpatterns = [
        # Progress status management URLs
        path('application/<int:application_id>/update_application_progress_status/<int:progress_status_id>/',
             update_application_progress_status.update_application_progress_status,
             name='update_application_progress_status'),  # Endpoint to update a progress status
    ]

    return progress_status_urlpatterns
