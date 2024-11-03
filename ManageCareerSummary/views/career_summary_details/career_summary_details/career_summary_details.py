# ManageCareerSummary/views/career_summary/career_summary_details/career_summary_details.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render

from ManageCareerSummary.models import MyCareerSummary
from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def career_summary_details(request, user_id, career_summary_id=None):
    try:
        user = request.user

        # Get or create the career summary
        career_summary = get_or_create_career_summary(request, user)

        context = {
                'urls_paths': urls_paths,
                'user': user,
                'career_summary': career_summary,
                'search_table': False,
                'content_details_mode': True,
                'career_summary_details_mode': True,
                'return_to_previous_page': return_to_previous_page,
            }

        return render(request, urls_paths['career_summary_details']['render'], context)
    except MyCareerSummary.DoesNotExist:
        log_error("No career summary found for the user.")
        return HttpResponseServerError("No career summary found for the user.")
    except Exception as e:
        log_error(f"An error occurred in the career_summary_details view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
