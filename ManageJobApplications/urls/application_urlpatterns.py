# ManageJobApplications/urls/application_urlpatterns.py
from django.urls import path

def get_application_urlpatterns():
    """
    Retrieve URL patterns for application-related views.

    This function defines URL patterns for views related to job applications, including
    adding, updating, deleting, and viewing application details.

    Returns:
        list: A list of URL patterns for application-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.applications.add_application_auto import add_application_auto
    from ManageJobApplications.views.applications.application_details import application_details
    from ManageJobApplications.views.applications.application_list import application_list
    from ManageJobApplications.views.applications.confirm_delete_application import confirm_delete_application
    from ManageJobApplications.views.applications.update_application import update_application

    # Define URL patterns
    return [

        # Application key management URLs
        path('user/<int:user_id>/application_list/',
             application_list.application_list, name='application_list'),

        path('user/<int:user_id>/application_details/<int:application_id>/',
             application_details.application_details, name='application_details'),

        path('user/<int:user_id>/add_application_auto/',
             add_application_auto.add_application_auto, name='add_application_auto'),

        path('user/<int:user_id>/update_application/<int:application_id>/',
             update_application.update_application, name='update_application'),

        path('user/<int:user_id>/confirm_delete_application/<int:application_id>/',
             confirm_delete_application.confirm_delete_application,
             name='confirm_delete_application'),

    ]

