# ManageAssistant/views/assistant/create_or_update_career_summary.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def generate_career_summary(request, user_id):
    try:
        user = request.user

        # Get or create the career summary
        career_summary = get_or_create_career_summary(request, user)

        if career_summary:
            print('\nCareer summary message saved (Auto)')

            return redirect(urls_paths['career_summary_details']['redirect'],
                            user_id=user.pk, career_summary_id=career_summary.pk)
        else:

            create_or_update_session(request, 'alert_message',
                                     'Failed to generate career summary.'
                                     '\nIt can be because you do not have any job profile or Projects.'
                                     '\nPlease do add them so career summary can be generated')
            print('\nFailed to generate career summary.')

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'career_summary': career_summary.career_summary if career_summary else None,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['career_summary_details']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the create_or_update_career_summary view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
