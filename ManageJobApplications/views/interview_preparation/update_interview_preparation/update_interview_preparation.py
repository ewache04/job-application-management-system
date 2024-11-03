# ManageJobApplications/views/interview_preparation/update_interview_preparation/update_interview_preparation.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import InterviewPreparation
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_interview_preparation(request, application_id, interview_preparation_id):
    try:
        user = request.user
        interview_preparation = get_object_or_404(InterviewPreparation, pk=interview_preparation_id)
        application = interview_preparation.application

        if request.method == 'POST':
            about_company = request.POST.get('about_company')
            prep_questions = request.POST.get('prep_questions')

            if about_company and prep_questions:
                interview_preparation.about_company = about_company
                interview_preparation.prep_questions = prep_questions
                interview_preparation.save()
                print('\nInterview Preparation updated')

                create_or_update_session(request, 'alert_message',
                                         'Your Interview Preparation has been updated successfully.')

                return redirect(urls_paths['interview_preparation_details']['redirect'],
                                application_id=application.pk, interview_preparation_id=interview_preparation.pk)

        context = {
            'user': user,
            'interview_preparation': interview_preparation,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['update_interview_preparation']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
