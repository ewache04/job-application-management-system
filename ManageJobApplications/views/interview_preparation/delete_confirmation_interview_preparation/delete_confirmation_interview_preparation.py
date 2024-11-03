# ManageJobApplications/views/interview_preparation/delete_interview_preparation/delete_interview_preparation.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import InterviewPreparation, JobApplication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def delete_confirmation_interview_preparation(request, application_id, interview_preparation_id):
    try:
        user = request.user
        interview_preparation = get_object_or_404(InterviewPreparation, pk=interview_preparation_id)
        application = interview_preparation.application

        if request.method == 'POST':
            interview_preparation.delete()
            create_or_update_session(request, 'alert_message',
                                     'Your Interview Preparation has been deleted successfully.')

            return redirect(urls_paths['interview_preparation_list']['redirect'],
                            application_id=application.pk)
        else:
            context = {
                'user': user,
                'urls_paths': urls_paths,
                'application': application,
                'interview_preparation': interview_preparation,
                'search_table': False,
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['delete_confirmation_interview_preparation']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
