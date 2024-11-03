# ManageAssistant/views/assistant/assistant_settings_detail.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render
from ManageAssistant.models import OpenAIAssistantSettings
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def assistant_settings_detail(request, user_id=None, assistant_id=None):
    try:

        user = request.user
        settings_obj = OpenAIAssistantSettings.objects.get(pk=assistant_id, user=user)

        print(settings_obj)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'settings': settings_obj,
            'search_table': False,
            'content_details_mode': True,
            'assistant_settings_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['assistant_settings_detail']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the assistant_settings_detail view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
