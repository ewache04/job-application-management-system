# ManageAssistant/urls.py

"""
URL configuration for the ManageAssistant app.

This module defines a function to initialize URL patterns for the ManageAssistant app.

The `initialize_urlpatterns` function imports URL patterns from the assistant_urlpatterns module,
adds them to the urlpatterns list, and returns the complete list.

Example:
    urlpatterns = initialize_urlpatterns()

Functions:
    initialize_urlpatterns: A function to initialize URL patterns for the ManageAssistant app.
"""


def initialize_urlpatterns():
    """
    Initialize URL patterns for the ManageAssistant app.

    This function initializes URL patterns for the ManageAssistant app by importing URL patterns
    from the assistant_urlpatterns module and adding them to the urlpatterns list.

    Returns:
        list: A list of URL patterns for the ManageAssistant app.
    """

    # Import the necessary modules
    from ManageAssistant.urls.assistant_urlpatterns import get_assistant_urlpatterns

    print("Initializing assistant URL patterns")

    urlpatterns = []

    # Add assistant URL patterns
    urlpatterns += get_assistant_urlpatterns()

    print("Completed initializing URL patterns")

    return urlpatterns
