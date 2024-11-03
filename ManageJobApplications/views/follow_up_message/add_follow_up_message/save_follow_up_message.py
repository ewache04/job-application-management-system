from django.db import IntegrityError
from django.http import request

from ManageJobApplications.models import FollowUpMessage
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from general_utils.error_logging import log_error


def save_follow_up_message(application, user, valid_follow_up_message_data):
    """
    Create a follow-up message for the given application and user if the data is valid.

    Parameters:
    - application: The application to which the follow-up message belongs.
    - user: The user who owns the follow-up message.
    - valid_follow_up_message_data: A dictionary containing the validated follow-up message data.

    Returns:
    - The created FollowUpMessage object if successful, None otherwise.
    """
    try:
        if valid_follow_up_message_data:
            follow_up_message = FollowUpMessage.objects.create(
                application=application,
                user=user,
                receivers_email='example@gmail.com',
                follow_up_message_subject=valid_follow_up_message_data.get('follow_up_message_subject'),
                follow_up_message=valid_follow_up_message_data.get('follow_up_message'),
                scheduled_send_date=None,
            )
            return follow_up_message
        else:
            return None
    except IntegrityError as e:
        log_error(f"Integrity error while creating follow-up message: {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error while creating follow-up message: {str(e)}")

    return None
