from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.forms.cover_letter_form.cover_letter_form import CoverLetterForm
from ManageJobApplications.models import JobApplication, CoverLetter
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_cover_letter(request, application_id, cover_letter_id):

    try:
        user = request.user
        cover_letter = get_object_or_404(CoverLetter, pk=cover_letter_id, user=user)
        application = cover_letter.application

        if request.method == 'POST':
            form = CoverLetterForm(request.POST, instance=cover_letter)
            if form.is_valid():
                form.save()
                create_or_update_session(request, 'alert_message',
                                         'Your cover letter has been updated successfully.')
                return redirect(urls_paths['cover_letter_details']['redirect'],
                                application_id=application.pk, cover_letter_id=cover_letter.pk)
        else:
            form = CoverLetterForm(instance=cover_letter)

        context = {
            'form': form,
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'return_to_previous_page': return_to_previous_page,
            'cover_letter': cover_letter,
        }
        return render(request, urls_paths['update_cover_letter']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
