# ManageJobApplications/views/resume/delete_confirmation_resume/delete_confirmation_resume.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import Resume
from ManageJobApplications.views.documents.get_last_document import get_last_document
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_resume(request, application_id, resume_id):
    try:
        user = request.user
        resume = get_object_or_404(Resume, pk=resume_id, user=user)
        application = resume.application

        document = get_last_document(application, 'resume')

        if request.method == 'POST':
            try:
                # Delete both the resume and the associated document
                if document:
                    document.delete()

                if resume:
                    resume.delete()

                create_or_update_session(request, 'alert_message', 'Your resume has been deleted successfully.')
                return redirect(urls_paths['application_details']['redirect'], pk=application.pk)

            except Exception as e:
                log_error(f"An error occurred while deleting the resume and associated document: {str(e)}")
                create_or_update_session(request, 'alert_message',
                                         'An error occurred while deleting the resume. Please try again later.')
                return redirect(urls_paths['application_details']['redirect'], pk=application.pk)

        else:
            context = {
                'user': user,
                'urls_paths': urls_paths,
                'application': application,
                'resume': resume,
                'search_table': False,
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['delete_confirmation_resume']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")