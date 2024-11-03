# ManageJobApplications/views/application_credentials/delete_confirmation_application_credential/delete_confirmation_application_credential.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import JobApplication, ApplicationCredential
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_application_credential(request, application_id, credential_id):
    try:
        user = request.user

        credential = get_object_or_404(ApplicationCredential, user=user, pk=credential_id)
        application = credential.application

        if request.method == 'POST':
            credential.delete()
            create_or_update_session(request, 'alert_message', 'Your credentials have been deleted successfully.')
            return redirect(urls_paths['application_credentials_list']['redirect'],
                            application_id=application.pk)

        context = {
            'application': application,
            'credential': credential,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['delete_confirmation_application_credential']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the delete_confirmation_application_credential view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
