from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageJobApplications.models import Contact
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def contact_details(request, application_id, contact_id):
    try:
        user = request.user
        contact = get_object_or_404(Contact, pk=contact_id, user=user)
        application = contact.application

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'contact': contact,
            'search_table': False,
            'content_details_mode': True,
            'contact_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['contact_details']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
