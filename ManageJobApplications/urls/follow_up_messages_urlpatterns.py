# ManageJobApplications/urls/follow_up_messages_urlpatterns.py
from django.urls import path


def get_follow_up_messages_urlpatterns():
    """
    Retrieve URL patterns for follow-up message-related views.

    This function defines URL patterns for managing follow-up messages, including adding, updating,
    deleting, and viewing details of follow-up messages.

    Returns:
        list: A list of URL patterns for follow-up message-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.follow_up_message.add_follow_up_message import add_follow_up_message
    from ManageJobApplications.views.follow_up_message.delete_confirmation_follow_up_message import \
        delete_confirmation_follow_up_message
    from ManageJobApplications.views.follow_up_message.follow_up_message_details import follow_up_message_details
    from ManageJobApplications.views.follow_up_message.follow_up_message_list import follow_up_message_list
    from ManageJobApplications.views.follow_up_message.update_follow_up_message import update_follow_up_message

    # Define URL patterns
    follow_up_messages_urlpatterns = [
        # Follow-up messages management URLs
        path('application/<int:application_id>/follow_up_message_list/',
             follow_up_message_list.follow_up_message_list,
             name='follow_up_message_list'),

        path('application/<int:application_id>/add_follow_up_message/',
             add_follow_up_message.add_follow_up_message,
             name='add_follow_up_message'),

        path('application/<int:application_id>/update_follow_up_message/<int:follow_up_message_id>/',
             update_follow_up_message.update_follow_up_message,
             name='update_follow_up_message'),

        path('application/<int:application_id>/delete_confirmation_follow_up_message/<int:follow_up_message_id>/',
             delete_confirmation_follow_up_message.delete_confirmation_follow_up_message,
             name='delete_confirmation_follow_up_message'),

        path('application/<int:application_id>/follow_up_message_details/<int:follow_up_message_id>/',
             follow_up_message_details.follow_up_message_details,
             name='follow_up_message_details'),
    ]

    return follow_up_messages_urlpatterns
