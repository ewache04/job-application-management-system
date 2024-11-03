# ManageCareerSummary/views/create_or_update_assistant_settings/generate_and_save_career_summary_message.py
from django.contrib.auth.models import User

from ManageCareerSummary.models import MyCareerSummary
from ManageCareerSummary.views.generate_career_summary.fetch_and_generate_career_summary import \
    fetch_and_generate_career_summary
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session


def generate_and_save_career_summary_message(client, user, career_summary_id=None):
    """
    Generate and save a career summary for a user.

    Args:
        client: The client object (type as per your implementation).
        user (User): The user object.
        career_summary_id (int, optional): The ID of an existing career summary to update.

    Returns:
        MyCareerSummary: The created or updated career summary object, or None if unsuccessful.
    """

    # Fetch job profiles, projects, and generate career summary
    career_summary = fetch_and_generate_career_summary(client, user)

    if career_summary:
        if career_summary_id is None:
            career_summary = MyCareerSummary.objects.create(
                user=user,
                career_summary=career_summary,
            )
        else:
            career_summary = MyCareerSummary.objects.filter(id=career_summary_id).update(
                user=user,
                career_summary=career_summary,
            )

        return career_summary
    else:
        return None
