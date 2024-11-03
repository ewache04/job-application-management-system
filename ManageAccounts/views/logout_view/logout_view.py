# Logout user
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

from ManageJobApplications.utils.thread_delay import thread_delay
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.session_utils.session_flush import session_flush
from OpenColabAI.settings import urls_paths

from general_utils.error_logging import log_error


def logout_view(request, user_id=None):
    try:

        # Clear session data
        session_flush(request.session)

        # Logout the user
        logout(request)

        # Optionally set an alert message for the user
        create_or_update_session(request.session, 'alert_message', 'You have been successfully logged out.')

        # Redirect to the index or login page
        return redirect(reverse(urls_paths['index']['redirect']))

    except Exception as e:
        # Log any errors if they occur during logout
        log_error(f"Error during logout: {str(e)}")
        return redirect(reverse(urls_paths['index']['redirect']))  # Redirect to index on error
