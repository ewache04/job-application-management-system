from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.forms.application_credential_form.application_credential_form import \
    ApplicationCredentialForm
from ManageJobApplications.models import JobApplication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths

from general_utils.error_logging import log_error
from general_utils.generate_password import generate_password
from return_to_previous_page import return_to_previous_page


@login_required
def add_application_credential(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        if request.method == 'POST':
            form = ApplicationCredentialForm(request.POST)
            if form.is_valid():
                credential = form.save(commit=False)
                credential.user = user
                credential.application = application
                credential.save()
                create_or_update_session(request, 'alert_message', 'Your credentials have been saved successfully.')
                return redirect(urls_paths['application_credential_details']['redirect'],
                                application_id=application.pk, credential_id=credential.pk)
        else:
            form = ApplicationCredentialForm()

        passwords = generate_password()

        password1 = passwords['secrets_password']
        password2 = passwords['passlib_password']

        print(password1, password1)

        context = {
            'form': form,
            'application': application,
            'password1': password1,
            'password2': password2,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['add_application_credential']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the add_application_credential view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
