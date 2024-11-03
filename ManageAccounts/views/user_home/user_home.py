# ManageAccounts/views/user_home/user_home.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ManageBackgroundLooks.views.create_or_update_backgroundlooks.set_selected_background import set_selected_background
from ManageJobApplications.models import JobApplication
from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def home(request, user_id=None):
    """
    Render the user's home page with job applications, career summary, and background settings.
    Also checks and updates the user's subscription status in the session.

    :param request: The HTTP request object.
    :param user_id: The ID of the user (optional).
    :return: Rendered HTML response for the user's home page.
    """
    user = request.user

    # Fetch job applications for the user, ordered by company name
    applications = JobApplication.objects.filter(user=user).order_by('company_name')

    # Get or create the career summary
    career_summary = get_or_create_career_summary(request, user)

    # Set the background color based on user settings
    background_color = set_selected_background(user, request)

    # Context to be passed to the template
    context = {
        'applications': applications,
        'urls_paths': urls_paths,
        'user': user,
        'career_summary': career_summary,
        'return_to_previous_page': return_to_previous_page,
        'background_color': background_color,
    }

    # Add additional context if there are job applications
    if applications.exists():
        context.update({
            "search_table": True,
            "application_list_mode": True,
            "list_display_mode": True,
        })

    # Render the user home page with the context
    return render(request, urls_paths['user_home']['render'], context)
