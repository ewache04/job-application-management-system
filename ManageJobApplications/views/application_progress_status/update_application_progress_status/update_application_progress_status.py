from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.forms.application_progress_status_form.application_progress_status_form import \
    ApplicationProgressStatusForm
from ManageJobApplications.models import ApplicationProgressStatus
from ManageJobApplications.utils.get_application_status import get_application_status
from ManageJobApplications.utils.get_interest_level import get_interest_level
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_application_progress_status(request, application_id, progress_status_id):
    try:
        user = request.user

        progress_status = get_object_or_404(ApplicationProgressStatus, pk=progress_status_id)
        application = progress_status.application

        if request.method == 'POST':
            form = ApplicationProgressStatusForm(request.POST, instance=progress_status)
            if form.is_valid():
                form.save()
                create_or_update_session(request, 'alert_message',
                                         'Your Job Application Progress Status has been updated successfully.')

                return redirect(urls_paths['application_details']['redirect'],
                                user_id=user.pk, application_id=application.pk)

        else:
            form = ApplicationProgressStatusForm(instance=progress_status)

        context = {
            'form': form,
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'progress_status': progress_status,
            'interest_level': get_interest_level(),
            'application_status': get_application_status(),
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['update_application_progress_status']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later.  {str(e)}")
