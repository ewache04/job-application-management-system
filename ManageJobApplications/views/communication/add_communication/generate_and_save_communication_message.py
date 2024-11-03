# ManageJobApplications/views/communication/add_communication/generate_and_save_follow_up_message.py
from django.contrib.auth.models import User
from django.http import HttpRequest

from ManageJobApplications.data_authentication_process.auth_communication_data.get_communication_message_form_data import \
    get_communication_message_form_data
from ManageJobApplications.models import Communication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session


def generate_and_save_communication_message(request: HttpRequest,
                                            client,
                                            user: User,
                                            application,
                                            company_message: str,
                                            applicant_message: str):
    """
    Generate and save a follow-up message for a job application.

    Args:
        request (HttpRequest): The HTTP request object.
        client: The client object (type as per your implementation).
        user (User): The user object.
        application (JobApplication): The job application object.
        company_message (str): The company message.
        applicant_message (str): The applicant message.
    """
    valid_communication_message_data = get_communication_message_form_data(
        client,
        user,
        company_message,
        applicant_message
    )

    if valid_communication_message_data:
        communication = Communication.objects.create(
            application=application,
            user=user,
            communication_subject=valid_communication_message_data.get('communication_subject'),
            communication_summary=valid_communication_message_data.get('communication_summary'),
        )

        return communication
    else:
        return None
