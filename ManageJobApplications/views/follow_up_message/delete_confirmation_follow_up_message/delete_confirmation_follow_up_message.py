from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ManageJobApplications.models import JobApplication, FollowUpMessage
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_follow_up_message(request, application_id, follow_up_message_id):
    try:
        user = request.user
        follow_up_message = get_object_or_404(FollowUpMessage, pk=follow_up_message_id, application__user=user)
        application = follow_up_message.application

        if request.method == 'POST':
            follow_up_message.delete()
            create_or_update_session(request, 'alert_message',
                                     'Your follow-up message has been deleted successfully.')

            return redirect(urls_paths['follow_up_message_list']['redirect'], application_id=application.pk)
        else:
            context = {
                'user': user,
                'urls_paths': urls_paths,
                'application': application,
                'follow_up_message': follow_up_message,
                'search_table': False,
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['delete_confirmation_follow_up_message']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
