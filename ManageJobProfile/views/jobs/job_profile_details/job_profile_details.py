from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageJobProfile.models import JobProfile
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def job_profile_details(request, user_id, job_profile_id):
    try:
        user = request.user

        job_profile = get_object_or_404(JobProfile, pk=job_profile_id, user=user)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'search_table': False,
            'content_details_mode': True,
            'job_profile_details_mode': True,
            'job_profile': job_profile,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['job_profile_details']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the job_profile_details view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
