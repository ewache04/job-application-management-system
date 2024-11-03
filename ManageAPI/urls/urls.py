# ManageAPI/urls.py
"""
URL configuration for the ManageAPI app.

This module defines a function to initialize URL patterns for the ManageAPI app.

The `initialize_urlpatterns` function imports URL patterns from the api_key_urlpatterns module,
adds them to the urlpatterns list, and returns the complete list.

Example:
    urlpatterns = initialize_urlpatterns()

Functions:
    initialize_urlpatterns: A function to initialize URL patterns for the ManageAPI app.
"""


def initialize_urlpatterns():
    """
    Initialize URL patterns for the ManageAPI app.

    This function initializes URL patterns for the ManageAPI app by importing URL patterns
    from the api_key_urlpatterns module and adding them to the urlpatterns list.

    Returns:
        list: A list of URL patterns for the ManageAPI app.
    """

    # Import the necessary modules
    from ManageAPI.urls.api_key_urlpatterns import get_api_key_urlpatterns

    print("Initializing api key URL patterns")

    urlpatterns = []

    # Add api key URL patterns
    urlpatterns += get_api_key_urlpatterns()

    print("Completed initializing URL patterns")

    return urlpatterns
