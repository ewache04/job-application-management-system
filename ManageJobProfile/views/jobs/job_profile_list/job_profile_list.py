from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render

from ManageJobProfile.models import JobProfile
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def job_profile_list(request, user_id=None):
    try:
        user = request.user

        job_profiles = JobProfile.objects.filter(user=user).order_by('id')

        context = {
            'job_profiles': job_profiles,
            'urls_paths': urls_paths,
            'user': user,
            'search_table': True,
            'list_display_mode': True,
            'job_profile_list_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['job_profile_list']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the job_profile_list view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
