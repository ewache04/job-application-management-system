from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render
from ManageJobApplications.models import JobApplication
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def application_list(request, user_id):
    try:

        user = request.user
        applications = JobApplication.objects.filter(user=user).order_by('-created_at')

        context = {
            'applications': applications,
            'urls_paths': urls_paths,
            'user': user,
            'search_table': True,
            'list_display_mode': True,
            'application_list_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['application_list']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the application_list view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
