# ManageJobApplications/views/job_profile_projects/job_profile_projects_list/job_profile_projects_list.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404

from ManageJobProfile.models import JobProfile, JobProfileProject
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def job_profile_projects_list(request, user_id, job_profile_id):
    try:
        user = request.user
        job_profile = get_object_or_404(JobProfile, user=user, pk=job_profile_id)
        job_profile_projects = JobProfileProject.objects.filter(job_profile=job_profile).order_by('id')

        context = {
            'user': user,
            'job_profile': job_profile,
            'job_profile_projects': job_profile_projects,
            'urls_paths': urls_paths,
            'search_table': True,
            'list_display_mode': True,
            'job_profile_project_list_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['job_profile_projects_list']['render'], context)

    except Exception as e:
        log_error(f"An error occurred in the job_profile_projects_list view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
