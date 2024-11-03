from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render, redirect

from ManageJobApplications.models import JobApplication, ApplicationCredential
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def application_credentials_list(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, user=user, pk=application_id)
        credentials = ApplicationCredential.objects.filter(application=application).order_by('created_at')

        # Determine if there are credentials
        credentials_exist = credentials.exists()

        context = {
            'application': application,
            'credentials': credentials,
            'search_table': True,
            'credentials_exist': credentials_exist,
            'list_display_mode': True,
            'credentials_list_mode': True,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['application_credentials_list']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the application_credentials_list view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
