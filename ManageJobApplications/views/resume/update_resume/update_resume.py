from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.forms.resume_form.resume_form import ResumeForm
from ManageJobApplications.models import Resume
from ManageJobApplications.views.documents.get_last_document import get_last_document
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_resume(request, application_id, resume_id):
    try:
        user = request.user
        resume = get_object_or_404(Resume, pk=resume_id, user=user)
        application = resume.application

        if request.method == 'POST':
            form = ResumeForm(request.POST, instance=resume)
            if form.is_valid():
                form.save()
                create_or_update_session(request, 'alert_message',
                                         'Your resume has been updated successfully.')

                return redirect(urls_paths['resume_details']['redirect'],
                                application_id=application.pk, resume_id=resume.pk)
        else:
            form = ResumeForm(instance=resume)

        context = {
            'form': form,
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'return_to_previous_page': return_to_previous_page,
            'resume': resume,
        }
        return render(request, urls_paths['update_resume']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
