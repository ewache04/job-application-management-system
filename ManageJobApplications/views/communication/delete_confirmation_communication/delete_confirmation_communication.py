from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ManageJobApplications.models import Communication, JobApplication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_communication(request, application_id, communication_id):
    try:
        user = request.user
        communication = get_object_or_404(Communication, pk=communication_id, user=user)
        application = communication.application

        if request.method == 'POST':
            communication.delete()
            create_or_update_session(request, 'alert_message',
                                     'Your Job Application Communication has been deleted successfully.')

            return redirect(urls_paths['communication_list']['redirect'], application_id=application.pk)
        else:
            context = {
                'user': user,
                'urls_paths': urls_paths,
                'application': application,
                'communication': communication,
                'search_table': False,
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['delete_confirmation_communication']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
