# ManageJobApplications/urls/communications_urlpatterns.py
from django.urls import path


def get_communications_urlpatterns():
    """
    Retrieve URL patterns for communication-related views.

    This function defines URL patterns for communication-related views, including adding,
    updating, deleting, and listing communications associated with job applications.

    Returns:
        list: A list of URL patterns for communication-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.communication.add_communication import add_communication
    from ManageJobApplications.views.communication.communication_details import communication_details
    from ManageJobApplications.views.communication.communication_list import communication_list
    from ManageJobApplications.views.communication.delete_confirmation_communication import \
        delete_confirmation_communication
    from ManageJobApplications.views.communication.update_communication import update_communication

    # Define URL patterns
    return [
        # Communications management URLs
        path('application/<int:application_id>/communication_list/', communication_list.communication_list,
             name='communication_list'),

        path('application/<int:application_id>/add_communication/',
             add_communication.add_communication, name='add_communication'),

        path('application/<int:application_id>/update_communication/<int:communication_id>/',
             update_communication.update_communication, name='update_communication'),

        path('application/<int:application_id>/delete_confirmation_communication/<int:communication_id>/',
             delete_confirmation_communication.delete_confirmation_communication,
             name='delete_confirmation_communication'),

        path('application/<int:application_id>/communication_details/<int:communication_id>/',
             communication_details.communication_details, name='communication_details'),
    ]
