# ManageAssistant/settings.py

import json
from ManageAssistant.models import OpenAIAssistantSettings


def get_assistant_settings():
    # Assuming there's only one instance of OpenAIAssistantSettings
    settings = OpenAIAssistantSettings.objects.first()

    # Create a dictionary to hold the settings
    return {
        "selected_model": settings.selected_model,
        'max_tokens': settings.max_tokens,
        "temperature": settings.temperature,
        "top_p": settings.top_p,
        "frequency_penalty": settings.frequency_penalty,
        "presence_penalty": settings.presence_penalty,

    }
