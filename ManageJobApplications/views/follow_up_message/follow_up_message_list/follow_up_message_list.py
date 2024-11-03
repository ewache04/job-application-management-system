from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageJobApplications.models import JobApplication, FollowUpMessage
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def follow_up_message_list(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, user=user, pk=application_id)
        follow_up_messages = FollowUpMessage.objects.filter(user=user, application=application).all()

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'follow_up_messages': follow_up_messages,
            'search_table': True,
            'list_display_mode': True,
            'follow_up_message_list_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['follow_up_message_list']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
