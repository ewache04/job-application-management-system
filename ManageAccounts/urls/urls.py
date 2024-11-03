# ManageAccounts/urls.py
"""
URL configuration for the ManageAccounts app.

This module defines a function to initialize URL patterns for the ManageAccounts app.

The `initialize_urlpatterns` function imports URL patterns from the user_urlpatterns module,
adds them to the urlpatterns list, and returns the complete list.

Example:
    urlpatterns = initialize_urlpatterns()

Functions:
    initialize_urlpatterns: A function to initialize URL patterns for the ManageAccounts app.
"""


def initialize_urlpatterns():
    """
    Initialize URL patterns for the ManageAccounts app.

    This function initializes URL patterns for the ManageAccounts app by importing URL patterns
    from the user_urlpatterns module and adding them to the urlpatterns list.

    Returns:
        list: A list of URL patterns for the ManageAccounts app.
    """
    # Import the necessary modules
    from ManageAccounts.urls.user_urlpatterns import get_user_urlpatterns

    print("Initializing account URL patterns")

    urlpatterns = []

    # Add user account URL patterns
    urlpatterns += get_user_urlpatterns()

    print("Completed initializing URL patterns")

    return urlpatterns
