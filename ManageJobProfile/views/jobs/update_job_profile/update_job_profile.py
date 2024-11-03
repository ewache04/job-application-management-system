from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobProfile.forms.job_profile_form.job_profile_form import JobProfileForm
from ManageJobProfile.models import JobProfile
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_job_profile(request, user_id, job_profile_id):
    try:
        user = request.user
        job_profile = get_object_or_404(JobProfile, pk=job_profile_id, user=user)

        if request.method == 'POST':
            form = JobProfileForm(request.POST, instance=job_profile)

            if form.is_valid():
                form.save()

                create_or_update_session(request, 'alert_message',
                                         'Your Job Profile has been updated successfully.')
                return redirect(urls_paths['job_profile_details']['redirect'],
                                user_id=user.pk, job_profile_id=job_profile_id)
        else:
            form = JobProfileForm(instance=job_profile)

        context = {
            'job_profile': job_profile,
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['update_job_profile']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the update_job_profile view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
