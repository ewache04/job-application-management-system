# ManageJobApplications/views/jobs/confirm_delete_job_profile/confirm_delete_job_profile.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobProfile.models import JobProfile
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def confirm_delete_job_profile(request, user_id, job_profile_id):
    try:
        user = request.user
        job_profile = get_object_or_404(JobProfile, pk=job_profile_id, user=user)

        if request.method == 'POST':
            job_profile.delete()
            create_or_update_session(request, 'alert_message',
                                     'Your Job Profile has been deleted successfully.')
            return redirect(urls_paths['job_profile_list']['redirect'], user_id=user.id)

        context = {
            'user': user,
            'job_profile': job_profile,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['confirm_delete_job_profile']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the delete_job_profile view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
