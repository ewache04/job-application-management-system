from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageJobApplications.models import JobApplication, Contact
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def contact_list(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, user=user, pk=application_id)
        contacts = Contact.objects.filter(application=application).all()

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'contacts': contacts,
            'search_table': True,
            'list_display_mode': True,
            'contact_list_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['contact_list']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
