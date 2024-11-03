# ManageJobApplications/urls/resume_urlpatterns.py
from django.urls import path


def get_resume_urlpatterns():
    """
    Retrieve URL patterns for resume-related views.

    This function defines URL patterns for managing resumes, including adding, updating,
    deleting, and viewing resume details.

    Returns:
        list: A list of URL patterns for resume-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.resume.add_resume.add_resume_auto import add_resume_auto
    from ManageJobApplications.views.resume.add_resume.add_resume_manual import add_resume
    from ManageJobApplications.views.resume.delete_confirmation_resume import delete_confirmation_resume
    from ManageJobApplications.views.resume.resume_details import resume_details
    from ManageJobApplications.views.resume.update_resume import update_resume

    # Define URL patterns
    resume_urlpatterns = [

        # Resume management URLs
        path('application/<int:application_id>/add_resume/',
             add_resume.add_resume, name='add_resume'),

        path('application/<int:application_id>/add_resume_auto/',
             add_resume_auto.add_resume_auto, name='add_resume_auto'),

        path('application/<int:application_id>/update_resume/<int:resume_id>/',
             update_resume.update_resume, name='update_resume'),

        path('application/<int:application_id>/delete_confirmation_resume/<int:resume_id>/',
             delete_confirmation_resume.delete_confirmation_resume,
             name='delete_confirmation_resume'),

        path('application/<int:application_id>/resume_details/<int:resume_id>/',
             resume_details.resume_details, name='resume_details'),
    ]

    return resume_urlpatterns
