# ManageJobApplications/views/follow_up_message/update_follow_up_message/update_follow_up_message.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ManageJobApplications.forms.follow_up_message_form.follow_up_message_form import FollowUpMessageForm
from ManageJobApplications.models import FollowUpMessage
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_follow_up_message(request, application_id, follow_up_message_id):
    try:
        user = request.user
        follow_up_message = get_object_or_404(FollowUpMessage, pk=follow_up_message_id)
        application = follow_up_message.application

        if request.method == 'POST':
            form = FollowUpMessageForm(request.POST, instance=follow_up_message)
            if form.is_valid():
                form.save()
                create_or_update_session(request, 'alert_message',
                                         'Your follow-up message has been updated successfully.')
                print(f"Follow-up message saved with pk: {follow_up_message.pk}")
                return redirect('follow_up_message_details',
                                application_id=follow_up_message.pk, follow_up_message_id=follow_up_message.id)
        else:
            form = FollowUpMessageForm(instance=follow_up_message)

        context = {
            'form': form,
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'return_to_previous_page': return_to_previous_page,
            'follow_up_message': follow_up_message,
        }
        return render(request, urls_paths['update_follow_up_message']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
