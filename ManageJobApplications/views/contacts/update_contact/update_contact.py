from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.forms.contact_update_form.contact_update_form import ContactUpdateForm
from ManageJobApplications.models import Contact
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_contact(request, application_id, contact_id):
    try:
        user = request.user
        contact = get_object_or_404(Contact, pk=contact_id, user=user)
        application = contact.application

        if request.method == 'POST':
            form = ContactUpdateForm(request.POST, instance=contact)
            if form.is_valid():
                form.save()
                print("Contact update was a success")
                create_or_update_session(request, 'alert_message',
                                         'Your Job Application Contact has been updated successfully.')
                return redirect(urls_paths['contact_details']['redirect'], application_id=application.pk, contact_id=contact.pk)
        else:
            form = ContactUpdateForm(instance=contact)

        context = {
            'form': form,
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'return_to_previous_page': return_to_previous_page,
            'contact': contact,
        }
        return render(request, urls_paths['update_contact']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
