# ManageAssistant/urls/assistant_urlpatterns.py

from django.urls import path


def get_assistant_urlpatterns():
    """
    Retrieve URL patterns for assistant-related views.

    This function defines URL patterns for assistant-related views, including settings update and details.

    Returns:
        list: A list of URL patterns for assistant-related views.
    """

    from ManageAssistant.views.assistant.assistant_settings_detail import assistant_settings_detail
    from ManageAssistant.views.assistant.create_or_update_assistant_settings import create_or_update_assistant_settings

    urlpatterns = [
        path('user/<int:user_id>/user_account/create_or_update_assistant_settings/<int:assistant_id>/',
             create_or_update_assistant_settings.create_or_update_assistant_settings,
             name='create_or_update_assistant_settings'),

        path('user/<int:user_id>/user_account/create_or_update_assistant_settings/',
             create_or_update_assistant_settings.create_or_update_assistant_settings,
             name='create_or_update_assistant_settings_no_id'),

        path('user/<int:user_id>/assistant_settings_detail/<int:assistant_id>/',
             assistant_settings_detail.assistant_settings_detail,
             name='assistant_settings_detail'),
    ]
    return urlpatterns
