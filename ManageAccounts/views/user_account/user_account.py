from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ManageAssistant.views.assistant.create_or_update_assistant_settings.generate_assistant_settings_url import \
    generate_assistant_settings_url
from ManageBackgroundLooks.views.create_or_update_backgroundlooks.generate_backgroundlooks_url import \
    generate_backgroundlooks_url
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


# View user details
@login_required
def user_account(request, user_id=None):
    user = request.user

    assistant_settings_url = generate_assistant_settings_url(user)

    backgroundlooks_url = generate_backgroundlooks_url(user)

    context = {
        'urls_paths': urls_paths,
        'user': user,
        'backgroundlooks_url': backgroundlooks_url,
        'assistant_settings_url': assistant_settings_url,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['user_account']['render'], context)
