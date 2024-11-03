# ManageJobApplications/views/cover_letter/add_cover_letter/add_cover_letter_manually.py
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from ManageJobApplications.forms.cover_letter_form.cover_letter_form import CoverLetterForm
from ManageJobApplications.models import JobApplication, Resume
from ManageJobApplications.views.cover_letter.add_cover_letter.generate_and_save_cover_letter import generate_and_save_cover_letter
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from openai_tools.initialize_openai_client import get_openai_client
from return_to_previous_page import return_to_previous_page


@login_required
def add_cover_letter(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        # Get or create the career summary
        career_summary = get_or_create_career_summary(request, user)

        resume = Resume.objects.filter(user=user).first()

        if request.method == 'POST':
            form = CoverLetterForm(request.POST)
            if form.is_valid():
                raw_cover_letter = form.cleaned_data.get('letter', '')

                client = get_openai_client(user)
                if client:
                    try:
                        cover_letter = generate_and_save_cover_letter(
                            request, client, user, application, career_summary, resume, raw_cover_letter
                        )
                        if cover_letter:
                            create_or_update_session(
                                request, 'alert_message', 'Your cover letter has been created successfully.'
                            )
                            return redirect(urls_paths['cover_letter_details']['redirect'],
                                            application_id=application.pk, cover_letter_id=cover_letter.pk)
                        else:
                            create_or_update_session(
                                request, 'alert_message', 'Your cover letter could not be created successfully. The '
                                                          'job description might be too long. Try again.'
                            )
                            return redirect(urls_paths['add_cover_letter']['redirect'], application_id=application.pk)
                    except Exception as e:
                        log_error(f"An error occurred while generating and saving the cover letter: {str(e)}")
                        create_or_update_session(
                            request, 'alert_message', 'An error occurred while generating the cover letter. Please try '
                                                      'again later.'
                        )
                        return redirect(urls_paths['add_cover_letter']['redirect'], application_id=application.pk)
                else:
                    log_error("OpenAI client is not available. Please make sure API key is correct.")
                    create_or_update_session(
                        request, 'alert_message', 'OpenAI client is not available. Please make sure API key is correct.'
                    )
                    return redirect(urls_paths['add_api_key']['redirect'])

        else:
            form = CoverLetterForm()

        context = {
            'user': user,
            'form': form,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['add_cover_letter']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
