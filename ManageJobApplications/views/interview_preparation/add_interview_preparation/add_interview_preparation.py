# ManageJobApplications/views/interview_preparation/add_interview_preparation/add_interview_preparation.py
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from ManageJobApplications.forms.interview_preparation_form.interview_preparation_form import InterviewPreparationForm
from ManageJobApplications.models import JobApplication
from ManageJobApplications.views.interview_preparation.add_interview_preparation.generate_and_save_interview_preparation import generate_and_save_interview_preparation

from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from openai_tools.initialize_openai_client import get_openai_client
from return_to_previous_page import return_to_previous_page


@login_required
def add_interview_preparation(request, application_id):
    """
    Handle the process of adding interview preparation automatically using OpenAI's assistant.

    Parameters:
    - request: The HTTP request object.
    - application_id: The ID of the job application for which the interview preparation is being added.

    Returns:
    - HTTPResponse: Renders the interview preparation addition page or redirects based on the form submission outcome.
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
            form = InterviewPreparationForm(request.POST, request.FILES)
            if form.is_valid():
                # Get the assistant-generated interview preparation content from the form
                about_company = str(form.cleaned_data.get('about_company', ''))
                prep_questions = str(form.cleaned_data.get('prep_questions', ''))
                raw_interview_preparation = str(about_company + prep_questions)

                # Initialize the OpenAI client for the user
                client = get_openai_client(user)
                if client:
                    try:
                        # Generate and save the interview preparation using the assistant
                        interview_preparation = generate_and_save_interview_preparation(request,
                                                                                        client, user,
                                                                                        application,
                                                                                        career_summary,
                                                                                        raw_interview_preparation)
                        if interview_preparation:
                            # If interview preparation creation is successful, set a success message and redirect to
                            # the interview preparation details page
                            print("Created interview preparation successfully")
                            create_or_update_session(request, 'alert_message', 'Your interview preparation has been '
                                                                               'created successfully.')
                            return redirect(urls_paths['interview_preparation_details']['redirect'],
                                            application_id=application.pk,
                                            interview_preparation_id=interview_preparation.pk)
                        else:
                            # If interview preparation creation fails, set an error message and redirect back to the
                            # interview preparation addition page
                            create_or_update_session(request, 'alert_message', 'Your interview preparation could not '
                                                                               'be created successfully. The job '
                                                                               'description might be too long. Try '
                                                                               'again.')
                            return redirect(urls_paths['add_interview_preparation']['redirect'],
                                            application_id=application.pk)
                    except Exception as e:
                        # Log any exceptions and set an error message
                        log_error(f"An error occurred while generating and saving the interview preparation: {str(e)}")
                        create_or_update_session(request, 'alert_message', 'An error occurred while generating the '
                                                                           'interview preparation. Please try again '
                                                                           'later.')
                        return redirect(urls_paths['add_interview_preparation']['redirect'],
                                        application_id=application.pk)
                else:
                    # Log an error if the OpenAI client is not available and set an error message
                    log_error("OpenAI client is not available. Please make sure API key is correct.")
                    create_or_update_session(request, 'alert_message', 'OpenAI client is not available. Please make '
                                                                       'sure API key is correct.')
                    return redirect(urls_paths['add_api_key']['redirect'])
        else:
            # Instantiate an empty form if the request method is not POST
            form = InterviewPreparationForm()

        # Define the context for rendering the template
        context = {
            'user': user,
            'form': form,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        # Render the template with the given context
        return render(request, urls_paths['add_interview_preparation']['render'], context)

    except Exception as e:
        # Log any exceptions and return a server error response
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
