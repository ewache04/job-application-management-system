# ManageAPI/urls/api_key_urlpatterns.py
from django.urls import path

from ManageAPI.views.add_api_key import add_api_key
from ManageAPI.views.api_key_details import api_key_details
from ManageAPI.views.api_key_list import api_key_list
from ManageAPI.views.confirm_delete_api_key import confirm_delete_api_key
from ManageAPI.views.update_api_key import update_api_key


def get_api_key_urlpatterns():
    """
    Retrieve URL patterns for API key management views.

    This function defines URL patterns for API key management views, including
    adding, updating, deleting, and listing API keys.

    Returns:
        list: A list of URL patterns for API key management views.
    """
    # Import necessary modules

    # Define URL patterns
    api_key_urlpatterns = [
        # API key management URLs
        path('user/<int:user_id>/user_account/api_key_list/', api_key_list.api_key_list, name='api_key_list'),

        path('user/<int:user_id>/user_account/add_api_key/', add_api_key.add_api_key, name='add_api_key'),

        path('user/<int:user_id>/user_account/edit/<int:api_key_id>/', update_api_key.update_api_key, name='update_api_key'),

        path('user/<int:user_id>/user_account/confirm_delete_api_key/<int:api_key_id>/',
             confirm_delete_api_key.confirm_delete_api_key, name='confirm_delete_api_key'),

        path('user/<int:user_id>/user_account/api_key_details/<int:api_key_id>/',
             api_key_details.api_key_details, name='api_key_details'),
    ]

    return api_key_urlpatterns
