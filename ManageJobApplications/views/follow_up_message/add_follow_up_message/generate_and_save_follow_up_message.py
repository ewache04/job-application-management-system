# ManageJobApplications/views/follow_up_message/add_follow_up_message/generate_and_save_follow_up_message.py
from ManageJobApplications.data_authentication_process.auth_follow_up_message_data.get_follow_up_message_form_data import \
    get_follow_up_message_form_data
from ManageJobApplications.views.follow_up_message.add_follow_up_message.save_follow_up_message import \
    save_follow_up_message

from general_utils.error_logging import log_error


def generate_and_save_follow_up_message(client, user, application=None, career_summary=None, resume=None,
                                        last_follow_up_message=None, new_follow_up_message=None):
    try:
        valid_follow_up_message_data = get_follow_up_message_form_data(client, user,
                                                                       application, career_summary,
                                                                       resume, last_follow_up_message,
                                                                       new_follow_up_message)

        if valid_follow_up_message_data:
            follow_up_message = save_follow_up_message(application, user, valid_follow_up_message_data)
            return follow_up_message
        else:
            return None

    except Exception as e:
        log_error(f"An error occurred while generating and saving the follow-up message: {str(e)}")
