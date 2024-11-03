# ManageBackgroundLooks/urls/urls.py

"""
URL configuration for the ManageBackgroundLooks app.

This module defines a function to initialize URL patterns for the ManageBackgroundLooks app.

The `initialize_urlpatterns` function imports URL patterns from the backgroundlooks_urlpatterns module,
adds them to the urlpatterns list, and returns the complete list.

Example:
    urlpatterns = initialize_urlpatterns()

Functions:
    initialize_urlpatterns: A function to initialize URL patterns for the ManageBackgroundLooks app.
"""


def initialize_urlpatterns():
    """
    Initialize URL patterns for the ManageBackgroundLooks app.

    This function initializes URL patterns for the ManageBackgroundLooks app by importing URL patterns
    from the backgroundlooks_urlpatterns module and adding them to the urlpatterns list.

    Returns:
        list: A list of URL patterns for the ManageBackgroundLooks app.
    """

    # Import the necessary modules
    from ManageBackgroundLooks.urls.backgroundlooks_urlpatterns import get_backgroundlooks_urlpatterns

    print("Initializing background look URL patterns")

    urlpatterns = []

    # Add background looks URL patterns
    urlpatterns += get_backgroundlooks_urlpatterns()

    print("Completed initializing URL patterns")

    return urlpatterns
