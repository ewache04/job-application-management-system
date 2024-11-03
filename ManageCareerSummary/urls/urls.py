# ManageCareerSummary/urls/urls.py

"""
URL configuration for the ManageCareerSummary app.

This module defines a function to initialize URL patterns for the ManageCareerSummary app.

The `initialize_urlpatterns` function imports URL patterns from the career_summary_urlpatterns module,
adds them to the urlpatterns list, and returns the complete list.

Example:
    urlpatterns = initialize_urlpatterns()

Functions:
    initialize_urlpatterns: A function to initialize URL patterns for the ManageCareerSummary app.
"""


def initialize_urlpatterns():
    """
    Initialize URL patterns for the ManageCareerSummary app.

    This function initializes URL patterns for the ManageCareerSummary app by importing URL patterns
    from the career_summary_urlpatterns module and adding them to the urlpatterns list.

    Returns:
        list: A list of URL patterns for the ManageCareerSummary app.
    """

    # Import the necessary modules
    from ManageCareerSummary.urls.career_summary_urlpatterns import get_career_summary_urlpatterns

    print("Initializing career summary URL patterns")

    urlpatterns = []

    # Add career summary URL patterns
    urlpatterns += get_career_summary_urlpatterns()

    print("Completed initializing URL patterns")

    return urlpatterns
