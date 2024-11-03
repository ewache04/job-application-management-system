# ManageJobApplications/urls/interview_preparation_urlpatterns.py
from django.urls import path


def get_interview_preparation_urlpatterns():
    """
    Retrieve URL patterns for interview preparation-related views.

    This function defines URL patterns for interview preparation-related views, including adding,
    updating, deleting, and listing interview preparations associated with job applications.

    Returns:
        list: A list of URL patterns for interview preparation-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.interview_preparation.add_interview_preparation import add_interview_preparation
    from ManageJobApplications.views.interview_preparation.delete_confirmation_interview_preparation import \
        delete_confirmation_interview_preparation
    from ManageJobApplications.views.interview_preparation.interview_preparation_details import \
        interview_preparation_details
    from ManageJobApplications.views.interview_preparation.interview_preparation_list import interview_preparation_list
    from ManageJobApplications.views.interview_preparation.update_interview_preparation import \
        update_interview_preparation

    # Define URL patterns
    return [

        # Interview Preparation management URLs
        path('application/<int:application_id>/interview_preparation_list/',
             interview_preparation_list.interview_preparation_list, name='interview_preparation_list'),

        path('application/<int:application_id>/add_interview_preparation/',
             add_interview_preparation.add_interview_preparation, name='add_interview_preparation'),

        path('application/<int:application_id>/update_interview_preparation/<int:interview_preparation_id>/',
             update_interview_preparation.update_interview_preparation, name='update_interview_preparation'),

        path(
            'application/<int:application_id>/delete_confirmation_interview_preparation/<int:interview_preparation_id>/',
            delete_confirmation_interview_preparation.delete_confirmation_interview_preparation,
            name='delete_confirmation_interview_preparation'),

        path('application/<int:application_id>/interview_preparation_details/<int:interview_preparation_id>/',
             interview_preparation_details.interview_preparation_details, name='interview_preparation_details'),
    ]
