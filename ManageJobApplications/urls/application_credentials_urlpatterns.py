# ManageJobApplications/urls/application_credentials_urlpatterns.py
from django.urls import path


def get_application_credentials_urlpatterns():
    """
    Retrieve URL patterns for managing application credentials.

    This function defines URL patterns for adding, viewing, updating, and deleting application credentials.

    Returns:
        list: A list of URL patterns for managing application credentials.
    """
    # Import necessary modules
    from ManageJobApplications.views.application_credentials.add_application_credential import \
        add_application_credential
    from ManageJobApplications.views.application_credentials.application_credential_details import \
        application_credential_details
    from ManageJobApplications.views.application_credentials.application_credentials_list import \
        application_credentials_list
    from ManageJobApplications.views.application_credentials.delete_confirmation_application_credential import \
        delete_confirmation_application_credential
    from ManageJobApplications.views.application_credentials.update_application_credential import \
        update_application_credential

    # Define URL patterns
    return [

        path('application/<int:application_id>/add_application_credential/',
             add_application_credential.add_application_credential,
             name='add_application_credential'),


        path('application/<int:application_id>/application_credentials_list/',
             application_credentials_list.application_credentials_list,
             name='application_credentials_list'),

        path('application/<int:application_id>/application_credential_details/<int:credential_id>/',
             application_credential_details.application_credential_details,
             name='application_credential_details'),

        path('application/<int:application_id>/update_application_credential/<int:credential_id>/',
             update_application_credential.update_application_credential,
             name='update_application_credential'),

        path('application/<int:application_id>/delete_confirmation_application_credential/<int:credential_id>/',
             delete_confirmation_application_credential.delete_confirmation_application_credential,
             name='delete_confirmation_application_credential'),
    ]
