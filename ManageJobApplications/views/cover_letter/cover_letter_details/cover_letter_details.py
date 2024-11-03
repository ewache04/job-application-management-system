# ManageJobApplications/views/cover_letter/cover_letter_details/cover_letter_details.py
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render, redirect

from ManageJobApplications.models import JobApplication, CoverLetter, Document
from ManageJobApplications.views.documents.get_last_document import get_last_document
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def cover_letter_details(request, application_id, cover_letter_id):
    application = None
    try:
        user = request.user
        cover_letter = get_object_or_404(CoverLetter, pk=cover_letter_id, user=user)
        application = cover_letter.application

        uploaded_cover_letter = get_last_document(application, 'cover_letter')

        if not cover_letter:
            create_or_update_session(request, 'alert_message', 'You do not have any cover letter. Please add one.')
            return redirect(urls_paths['add_cover_letter']['redirect'], application_id=application.pk)

        if uploaded_cover_letter and uploaded_cover_letter.file:
            uploaded_cover_letter_file_name = os.path.basename(uploaded_cover_letter.file.name)
        else:
            uploaded_cover_letter_file_name = None

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'cover_letter': cover_letter,
            'uploaded_cover_letter': uploaded_cover_letter,
            'uploaded_cover_letter_file_name': uploaded_cover_letter_file_name,
            'search_table': False,
            'content_details_mode': True,
            'cover_letter_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['cover_letter_details']['render'], context)

    except CoverLetter.DoesNotExist:
        create_or_update_session(request, 'alert_message', 'You do not have any cover letter. Please add one.')
        return redirect(urls_paths['add_cover_letter']['redirect'], application_id=application.pk)
    except Document.DoesNotExist:
        create_or_update_session(request, 'alert_message', 'You do not have any cover letter document. Please add one.')
        return redirect(urls_paths['add_cover_letter']['redirect'], application_id=application.pk)
    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
