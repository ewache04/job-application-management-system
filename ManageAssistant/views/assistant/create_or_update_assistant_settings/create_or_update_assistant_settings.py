# ManageAssistant/views/assistant/create_or_update_assistant_settings.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from ManageAssistant.forms.openai_assistant_settings_form.openai_assistant_settings_form import \
    OpenAIAssistantSettingsForm
from ManageAssistant.models import OpenAIAssistantSettings
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from openai_tools import openai_models
from return_to_previous_page import return_to_previous_page


@login_required
def create_or_update_assistant_settings(request, user_id, assistant_id=None):
    try:
        user = request.user

        if assistant_id:
            settings_obj = OpenAIAssistantSettings.objects.get(pk=assistant_id, user=user)
        else:
            settings_obj = OpenAIAssistantSettings(user=user)

        if request.method == 'POST':
            form = OpenAIAssistantSettingsForm(request.POST, instance=settings_obj)
            if form.is_valid():
                form.instance.user = user
                assistant = form.save()

                create_or_update_session(request, 'alert_message', 'Your Assistant settings have been created or '
                                                                   'updated successfully.')

                return redirect(urls_paths['assistant_settings_detail']['redirect'],
                                user_id=user.pk, assistant_id=assistant.pk)
        else:
            form = OpenAIAssistantSettingsForm(instance=settings_obj)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'settings': settings_obj,
            'openai_models': openai_models.get_openai_models(),
            'form': form,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['create_or_update_assistant_settings']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the create_or_update_assistant_settings view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
