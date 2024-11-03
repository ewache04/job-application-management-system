# ManageJobApplications/views/jobs/add_job_profile/add_job_profile.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render

from ManageJobProfile.forms.job_profile_form.job_profile_form import JobProfileForm
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def add_job_profile(request, user_id):
    try:
        user = request.user
        if request.method == 'POST':
            form = JobProfileForm(request.POST)

            if form.is_valid():
                job_profile = form.save(commit=False)
                job_profile.user = user
                job_profile.save()

                create_or_update_session(request, 'alert_message',
                                         'Your Job Profile has been created successfully.')

                return redirect(urls_paths['job_profile_details']['redirect'],
                                user_id=user.pk, job_profile_id=job_profile.pk)
        else:
            form = JobProfileForm()

        context = {
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['add_job_profile']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the add_job_profile view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
