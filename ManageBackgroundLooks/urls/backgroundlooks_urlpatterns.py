# ManageBackgroundLooks/urls/backgroundlooks_urlpatterns.py

from django.urls import path


def get_backgroundlooks_urlpatterns():
    """
    Retrieve URL patterns for career backgroundlooks-related views.

    This function defines URL patterns for backgroundlooks-related views, including update views.

    Returns:
        list: A list of URL patterns for career summary-related views.
    """
    from ManageBackgroundLooks.views.create_or_update_backgroundlooks import create_or_update_backgroundlooks
    from ManageBackgroundLooks.views.get_background_color import get_background_color

    urlpatterns = [

        path('user/<int:user_id>/user_account/create_or_update_backgroundlooks/<int:backgroundlooks_id>/',
             create_or_update_backgroundlooks.create_or_update_backgroundlooks,
             name='create_or_update_backgroundlooks'),

        path('user/<int:user_id>/user_account/create_or_update_backgroundlooks/',
             create_or_update_backgroundlooks.create_or_update_backgroundlooks,
             name='create_or_update_backgroundlooks_no_id'),

        path('user/<int:user_id>/get_background_color/',
             get_background_color.get_background_color, name='get_background_color')

    ]
    return urlpatterns
