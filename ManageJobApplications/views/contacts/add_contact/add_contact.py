from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ManageJobApplications.forms.contact_form.contact_form import ContactForm
from ManageJobApplications.models import JobApplication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def add_contact(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user = user
                contact.application = application
                contact.save()

                create_or_update_session(request, 'alert_message',
                                         'Your Job Application Contact has been created successfully.')

                return redirect(urls_paths['contact_details']['redirect'],
                                application_id=application.pk, contact_id=contact.pk)

        else:

            form = ContactForm()

        context = {
            'user': user,
            'form': form,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['add_contact']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
