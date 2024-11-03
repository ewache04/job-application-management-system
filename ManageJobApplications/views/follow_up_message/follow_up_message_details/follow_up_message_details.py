from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageJobApplications.models import FollowUpMessage
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def follow_up_message_details(request, application_id, follow_up_message_id):
    try:
        user = request.user

        follow_up_message = get_object_or_404(FollowUpMessage, pk=follow_up_message_id, user=user)
        application = follow_up_message.application

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'follow_up_message': follow_up_message,
            'search_table': False,
            'content_details_mode': True,
            'follow_up_message_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['follow_up_message_details']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
