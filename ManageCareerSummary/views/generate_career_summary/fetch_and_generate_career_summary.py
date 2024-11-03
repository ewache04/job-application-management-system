# ManageCareerSummary/views/create_or_update_assistant_settings/fetch_and_generate_career_summary.py
from ManageCareerSummary.assistant.career_summary.generate_career_summary import generate_career_summary
from ManageJobProfile.models import JobProfile, JobProfileProject

from openai_tools.initialize_openai_client import get_openai_client


def fetch_and_generate_career_summary(client, user):
    """
    Fetch job profiles and projects for the user, initialize the OpenAI client,
    and generate the career summary.

    Parameters:
    - user: User object containing user information.

    Returns:
    - career_summary: The generated career summary or None if unsuccessful.
    """
    try:
        job_profiles = JobProfile.objects.filter(user=user)
    except JobProfile.DoesNotExist:
        job_profiles = None

    try:
        projects = JobProfileProject.objects.filter(user=user)
    except JobProfileProject.DoesNotExist:
        projects = None

    if client and job_profiles:
        # Generate and save career summary
        career_summary = generate_career_summary(client, user, job_profiles, projects)
        print(career_summary)
        return career_summary
    else:
        return None
