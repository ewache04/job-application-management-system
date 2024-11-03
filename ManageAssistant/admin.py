# ManageAssistant/admin.py

from django.contrib import admin
from .models import OpenAIAssistantSettings


# Define your admin class for OpenAIAssistantSettings
class OpenAIAssistantSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'selected_model', 'max_tokens', 'temperature', 'top_p', 'frequency_penalty', 'presence_penalty')

    search_fields = ('user__username',)
    list_filter = ('selected_model',)
    readonly_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Settings', {
            'fields': (
                'selected_model', 'max_tokens', 'temperature', 'top_p',
                'frequency_penalty', 'presence_penalty')

        }),
    )


# Register OpenAIAssistantSettings with its admin class
admin.site.register(OpenAIAssistantSettings, OpenAIAssistantSettingsAdmin)
