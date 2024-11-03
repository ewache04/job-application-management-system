# ManageJobApplications/views/interview_preparation/interview_preparation_details/interview_preparation_details.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404

from ManageJobApplications.models import InterviewPreparation, JobApplication
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def interview_preparation_details(request, application_id, interview_preparation_id):
    try:
        user = request.user
        interview_preparation = get_object_or_404(InterviewPreparation, pk=interview_preparation_id)
        application = interview_preparation.application

        context = {
            'user': user,
            'urls_paths': urls_paths,
            'application': application,
            'interview_preparation': interview_preparation,
            'search_table': False,
            'content_details_mode': True,
            'interview_preparation_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['interview_preparation_details']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
