# ManageCareerSummary/urls/career_summary_urlpatterns.py

from django.urls import path


def get_career_summary_urlpatterns():
    """
    Retrieve URL patterns for career summary-related views.

    This function defines URL patterns for career summary-related views, including create/update and detail views.

    Returns:
        list: A list of URL patterns for career summary-related views.
    """
    from ManageCareerSummary.views.generate_career_summary import generate_career_summary
    from ManageCareerSummary.views.update_career_summary import update_career_summary
    from ManageCareerSummary.views.career_summary_details.career_summary_details import career_summary_details

    urlpatterns = [

        path('user/<int:user_id>/generate_career_summary/',
             generate_career_summary.generate_career_summary,
             name='generate_career_summary'),

        path('user/<int:user_id>/update_career_summary/<int:career_summary_id>/',
             update_career_summary.update_career_summary,
             name='update_career_summary'),

        path('user/<int:user_id>/career_summary_details/<int:career_summary_id>/',
             career_summary_details.career_summary_details, name='career_summary_details'),

    ]
    return urlpatterns
