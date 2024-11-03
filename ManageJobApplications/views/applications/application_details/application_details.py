# ManageJobApplications/views/application_credentials/application_credentials_list/application_credentials_list.py
import os
import traceback

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from ManageJobApplications.models import (JobApplication, ApplicationProgressStatus,
                                          CoverLetter, Resume, Communication, FollowUpMessage)

from ManageJobApplications.views.documents.get_last_document import get_last_document
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def application_details(request, user_id, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)
        progress_status = ApplicationProgressStatus.objects.get(application=application, user=user)

        # Get or create the career summary
        career_summary = get_or_create_career_summary(request, user)

        cover_letter = CoverLetter.objects.filter(application=application, user=user).last()
        resume = Resume.objects.filter(application=application, user=user).last()

        # Helper function to retrieve communication and follow-up message
        def get_latest_entry(model, application):
            try:
                return model.objects.filter(application=application).latest('id')
            except model.DoesNotExist:
                return None

        communication = get_latest_entry(Communication, application)
        follow_up_message = get_latest_entry(FollowUpMessage, application)

        uploaded_resume = get_last_document(application, 'resume')
        uploaded_cover_letter = get_last_document(application, 'cover_letter')

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'career_summary':career_summary,
            'application': application,
            'communication': communication,
            'follow_up_message': follow_up_message,
            'cover_letter': cover_letter,
            'resume': resume,
            'uploaded_resume': uploaded_resume,
            'uploaded_cover_letter': uploaded_cover_letter,
            'uploaded_resume_file_name': uploaded_resume.file.name.split('/')[-1] if uploaded_resume else None,
            # Extract filename without path
            'uploaded_cover_letter_file_name': uploaded_cover_letter.file.name.split('/')[
                -1] if uploaded_cover_letter else None,  # Extract filename
            'progress_status': progress_status,
            'search_table': False,
            'content_details_mode': True,
            'application_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['application_details']['render'], context)

    except Exception as e:
        log_error(f"An error occurred in the application_details view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
