# ManageJobApplications/views/resume/add_resume/add_resume_auto/add_resume_auto.py
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from ManageJobApplications.forms.resume_form.resume_form import ResumeForm
from ManageJobApplications.models import JobApplication
from ManageJobApplications.views.resume.add_resume.add_resume_auto.generate_and_save_resume import (
    generate_and_save_resume
)
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from openai_tools.initialize_openai_client import get_openai_client
from return_to_previous_page import return_to_previous_page


@login_required
def add_resume_auto(request, application_id):
    """
    Handle the process of adding a resume automatically using OpenAI's assistant.

    Parameters:
    - request: The HTTP request object.
    - application_id: The ID of the job application for which the resume is being added.

    Returns:
    - HTTPResponse: Renders the resume addition page or redirects based on the form submission outcome.
    """
    try:
        # Get the current user
        user = request.user

        # Fetch the job application for the given user and application ID
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        # Get or create the career summary
        career_summary = get_or_create_career_summary(request, user)

        if request.method == 'POST':
            # Instantiate the form with POST data and file uploads
            form = ResumeForm(request.POST, request.FILES)
            if form.is_valid():
                # Get the assistant-generated resume content from the form
                raw_resume = form.cleaned_data.get('assistant_resume', '')

                # Initialize the OpenAI client for the user
                client = get_openai_client(user)
                if client:
                    try:
                        # Generate and save the resume using the assistant
                        resume = generate_and_save_resume(request, client, user,
                                                          application,
                                                          career_summary, raw_resume)
                        if resume:
                            # If resume creation is successful, set a success message and redirect to the resume
                            # details page
                            create_or_update_session(request, 'alert_message',
                                                     'Your resume has been created successfully.')
                            return redirect(urls_paths['resume_details']['redirect'], application_id=application.pk,
                                            resume_id=resume.pk)
                        else:
                            # If resume creation fails, set an error message and redirect back to the resume addition
                            # page
                            create_or_update_session(request, 'alert_message',
                                                     'Your resume could not be created successfully. The job '
                                                     'description might be too long. Try again.')
                            return redirect(urls_paths['add_resume_auto']['redirect'], application_id=application.pk)
                    except Exception as e:
                        # Log any exceptions and set an error message
                        log_error(f"An error occurred while generating and saving the resume: {str(e)}")
                        create_or_update_session(request, 'alert_message',
                                                 'An error occurred while generating the resume. Please try again '
                                                 'later.')
                        return redirect(urls_paths['add_resume_auto']['redirect'], application_id=application.pk)
                else:
                    # Log an error if the OpenAI client is not available and set an error message
                    log_error("OpenAI client is not available. Please make sure API key is correct.")
                    create_or_update_session(request, 'alert_message',
                                             'OpenAI client is not available. Please make sure API key is correct.')
                    return redirect(urls_paths['add_api_key']['redirect'])
        else:
            # Instantiate an empty form if the request method is not POST
            form = ResumeForm()

        # Define the context for rendering the template
        context = {
            'user': user,
            'form': form,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        # Render the template with the given context
        return render(request, urls_paths['add_resume_auto']['render'], context)

    except Exception as e:
        # Log any exceptions and return a server error response
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
