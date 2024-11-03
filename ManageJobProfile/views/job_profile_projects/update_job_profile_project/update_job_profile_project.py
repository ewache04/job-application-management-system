# ManageJobApplications/views/job_profile_projects/update_job_profile_project/update_job_profile_project.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobProfile.forms.job_profile_projects_form.job_profile_project_form import JobProfileProjectForm
from ManageJobProfile.models import JobProfileProject
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_job_profile_project(request, user_id, job_profile_id, job_profile_project_id):
    try:
        user = request.user
        job_profile_project = get_object_or_404(JobProfileProject, pk=job_profile_project_id, user=user)
        job_profile = job_profile_project.job_profile

        if request.method == 'POST':
            form = JobProfileProjectForm(request.POST, instance=job_profile_project)

            if form.is_valid():
                form.save()

                create_or_update_session(request, 'alert_message',
                                         'Your Job project has been updated successfully.')
                return redirect(urls_paths['job_profile_project_details']['redirect'],
                                user_id=user.pk,
                                job_profile_id=job_profile.pk,
                                job_profile_project_id=job_profile_project.pk)
        else:
            form = JobProfileProjectForm(instance=job_profile_project)

        context = {
            'job_profile': job_profile,
            'job_profile_project': job_profile_project,
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['update_job_profile_project']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the update_job_profile view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
