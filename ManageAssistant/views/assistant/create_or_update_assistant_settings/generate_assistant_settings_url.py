# ManageAssistant/views/assistant/create_or_update_assistant_settings/generate_assistant_settings_url.py
from django.urls import reverse

from ManageAssistant.models import OpenAIAssistantSettings


def generate_assistant_settings_url(user):
    try:
        settings_obj = OpenAIAssistantSettings.objects.get(user=user)
        url = reverse('create_or_update_assistant_settings',
                      kwargs={'user_id': user.pk, 'assistant_id': settings_obj.pk})
    except OpenAIAssistantSettings.DoesNotExist:
        url = reverse('create_or_update_assistant_settings_no_id', kwargs={'user_id': user.pk})
    return url
