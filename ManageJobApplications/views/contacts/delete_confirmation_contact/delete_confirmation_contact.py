from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import JobApplication, Contact
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_contact(request, application_id, contact_id):
    try:
        user = request.user
        contact = get_object_or_404(Contact, pk=contact_id, user=user)
        application = contact.application

        if request.method == 'POST':

            contact.delete()
            create_or_update_session(request, 'alert_message',
                                     'Your Job Application Contact has been deleted successfully.')

            return redirect(urls_paths['contact_list']['redirect'], application_id=application.pk)

        else:
            context = {
                'user': user,
                'urls_paths': urls_paths,
                'application': application,
                'contact': contact,
                'search_table': False,
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['delete_confirmation_contact']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
