from ManageCareerSummary.models import MyCareerSummary
from ManageCareerSummary.views.generate_career_summary.generate_and_save_career_summary_message import \
    generate_and_save_career_summary_message
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from openai_tools.initialize_openai_client import get_openai_client


def get_or_create_career_summary(request, user):
    """
    Retrieves or generates and stores the career summary for a given user.

    :param request: HttpRequest object
    :param user: User object
    :return: MyCareerSummary object
    """
    # Get OpenAI client for the user
    client = get_openai_client(user)

    # Retrieve the career summary from the database
    try:
        career_summary = MyCareerSummary.objects.filter(user_id=user.id).latest('created_at')
    except MyCareerSummary.DoesNotExist:
        career_summary = None

    # Generate career summary if not found
    if not career_summary:
        career_summary = generate_and_save_career_summary_message(
            client,
            user,
            career_summary_id=None,
        )

    return career_summary
