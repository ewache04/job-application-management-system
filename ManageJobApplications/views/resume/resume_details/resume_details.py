# ManageJobApplications/views/resume/resume_details/resume_details.py
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render, redirect

from ManageJobApplications.models import JobApplication, Resume, Document
from ManageJobApplications.views.documents.get_last_document import get_last_document
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def resume_details(request, application_id, resume_id):
    application = None
    try:
        user = request.user
        resume = get_object_or_404(Resume, pk=resume_id, user=user)
        application = resume.application

        uploaded_resume = get_last_document(application, 'resume')

        if not resume:
            create_or_update_session(request, 'alert_message', 'You do not have any resume. Please add one.')
            return redirect(urls_paths['add_resume_auto']['redirect'], application_id=application.pk)

        if uploaded_resume and uploaded_resume.file:
            uploaded_resume_file_name = os.path.basename(uploaded_resume.file.name)
        else:
            uploaded_resume_file_name = None

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'resume': resume,
            'uploaded_resume': uploaded_resume,
            'uploaded_resume_file_name': uploaded_resume_file_name,
            'search_table': False,
            'content_details_mode': True,
            'resume_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['resume_details']['render'], context)

    except Resume.DoesNotExist:
        create_or_update_session(request, 'alert_message', 'You do not have any resume. Please add one.')
        return redirect(urls_paths['add_resume_auto']['redirect'], application_id=application.pk)
    except Document.DoesNotExist:
        create_or_update_session(request, 'alert_message', 'You do not have any resume document. Please add one.')
        return redirect(urls_paths['add_resume_auto']['redirect'], application_id=application.pk)
    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
