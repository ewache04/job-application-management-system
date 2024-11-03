# ManageJobApplications/views/communication/update_communication.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ManageJobApplications.forms.communication_form.communication_form import CommunicationForm
from ManageJobApplications.models import Communication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_communication(request, application_id, communication_id):
    try:
        user = request.user
        communication = get_object_or_404(Communication, pk=communication_id)
        application = communication.application

        if request.method == 'POST':
            form = CommunicationForm(request.POST, instance=communication)
            if form.is_valid():
                form.save()
                create_or_update_session(request, 'alert_message',
                                         'Your Job Application Communication has been updated successfully.')

                print(f"Communication message saved with pk: {communication.pk}")
                return redirect(urls_paths['communication_details']['redirect'],
                                application_id=application.pk, communication_id=communication.pk)

        else:
            form = CommunicationForm(instance=communication)

        context = {
            'user': user,
            'communication': communication,
            'application': application,
            'urls_paths': urls_paths,
            'form': form,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['update_communication']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
