from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

from ManageJobApplications.forms.application_credential_form.application_credential_form import \
    ApplicationCredentialForm
from ManageJobApplications.models import ApplicationCredential, JobApplication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from general_utils.generate_password import generate_password
from return_to_previous_page import return_to_previous_page


@login_required
def update_application_credential(request, application_id, credential_id):
    try:
        user = request.user

        credential = get_object_or_404(ApplicationCredential, user=user, pk=credential_id)
        application = credential.application

        if request.method == 'POST':
            form = ApplicationCredentialForm(request.POST, instance=credential)
            if form.is_valid():

                form.save()
                create_or_update_session(request, 'alert_message', 'Your credentials have been updated successfully.')

                return redirect(urls_paths['application_credential_details']['redirect'],
                                application_id=application.pk, credential_id=credential.pk)
        else:
            form = ApplicationCredentialForm(instance=credential)

        passwords = generate_password()

        password1 = passwords['secrets_password']
        password2 = passwords['passlib_password']

        context = {
            'form': form,
            'password1': password1,
            'password2': password2,
            'credential': credential,
            'application': application,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['update_application_credential']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the update_application_credential view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
