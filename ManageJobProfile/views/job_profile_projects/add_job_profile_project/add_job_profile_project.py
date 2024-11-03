# ManageJobApplications/views/job_profile_projects/add_job_profile_project/add_job_profile_project.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render

from ManageJobProfile.forms.job_profile_projects_form.job_profile_project_form import JobProfileProjectForm
from ManageJobProfile.models import JobProfile
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def add_job_profile_project(request, user_id, job_profile_id):
    try:
        user = request.user
        job_profile = JobProfile.objects.get(pk=job_profile_id)
        if request.method == 'POST':
            form = JobProfileProjectForm(request.POST)

            if form.is_valid():
                job_profile_project = form.save(commit=False)
                job_profile_project.user = user
                job_profile_project.job_profile = job_profile
                job_profile_project.save()

                create_or_update_session(request, 'alert_message',
                                         'Your project has been created successfully.')

                return redirect(urls_paths['job_profile_project_details']['redirect'],
                                user_id=user.pk,
                                job_profile_id=job_profile.pk,
                                job_profile_project_id=job_profile_project.pk)
        else:
            form = JobProfileProjectForm()

        context = {
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'job_profile': job_profile,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['add_job_profile_project']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the add_job_profile view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
