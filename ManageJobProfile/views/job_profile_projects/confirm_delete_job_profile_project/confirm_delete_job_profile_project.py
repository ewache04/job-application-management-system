# ManageJobApplications/views/job_profile_projects/confirm_delete_job_profile_project/confirm_delete_job_profile_project.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobProfile.models import JobProfileProject
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def confirm_delete_job_profile_project(request, user_id, job_profile_id, job_profile_project_id):
    try:
        user = request.user
        job_profile_project = get_object_or_404(JobProfileProject, pk=job_profile_project_id, user=user)
        job_profile = job_profile_project.job_profile

        if request.method == 'POST':
            job_profile_project.delete()
            create_or_update_session(request, 'alert_message',
                                     'Your project has been deleted successfully.')

            return redirect(urls_paths['job_profile_projects_list']['redirect'],
                            user_id=user.pk, job_profile_id=job_profile.pk)

        context = {
            'user': user,
            'job_profile': job_profile,
            'job_profile_project': job_profile_project,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['confirm_delete_job_profile_project']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the delete_job_profile view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
