from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.forms.resume_form.resume_form import ResumeForm
from ManageJobApplications.models import JobApplication, Resume
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def add_resume(request, application_id):

    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        resume = Resume.objects.filter(application=application, user=user).last()

        # Check if a resume already exists for this application
        if resume.exists():
            create_or_update_session(request, 'alert_message', 'A resume already exists for this application.')
            return redirect(urls_paths['resume_details']['redirect'],
                            application_id=application.pk, resume_id=resume.pk)

        if request.method == 'POST':
            form = ResumeForm(request.POST)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.user = user
                resume.application = application
                resume.save()

                create_or_update_session(request, 'alert_message',
                                         'Your resume has been created successfully.')

                return redirect(urls_paths['resume_details']['redirect'],
                                application_id=application.pk, resume_id=resume.pk)
        else:
            form = ResumeForm()

        context = {
            'user': user,
            'form': form,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['add_resume']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
