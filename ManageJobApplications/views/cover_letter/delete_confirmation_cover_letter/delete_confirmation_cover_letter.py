from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import JobApplication, CoverLetter, Document
from ManageJobApplications.views.documents.get_last_document import get_last_document
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_cover_letter(request, application_id, cover_letter_id):
    try:
        user = request.user
        cover_letter = get_object_or_404(CoverLetter, pk=cover_letter_id, user=user)
        application = cover_letter.application

        document = get_last_document(application, 'cover_letter')

        if request.method == 'POST':
            try:
                # Delete both the cover letter and the associated document
                if document:
                    document.delete()

                if cover_letter:
                    cover_letter.delete()

                create_or_update_session(request, 'alert_message', 'Your cover letter has been deleted successfully.')
                return redirect(urls_paths['application_details']['redirect'], pk=application.pk)

            except Exception as e:
                log_error(f"An error occurred while deleting the cover letter and associated document: {str(e)}")
                create_or_update_session(request, 'alert_message',
                                         'An error occurred while deleting the cover letter. Please try again later.')
                return redirect(urls_paths['application_details']['redirect'], pk=application.pk)

        else:
            context = {
                'user': user,
                'urls_paths': urls_paths,
                'application': application,
                'cover_letter': cover_letter,
                'search_table': False,
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['delete_confirmation_cover_letter']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
