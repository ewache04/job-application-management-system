# ManageAPI/views/update_api_key/update_api_key.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from ManageAPI.forms.user_key_form.user_key_form import UserKeyForm
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from ManageAPI.models import UserKey
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_api_key(request, user_id, api_key_id):
    user = request.user
    try:
        key = get_object_or_404(UserKey, pk=api_key_id, user=user)
        if request.method == 'POST':
            form = UserKeyForm(request.POST, instance=key)
            if form.is_valid():
                form.save()
                create_or_update_session(request, 'alert_message', 'Your API Key has been updated successfully.')
                return redirect(urls_paths['api_key_details']['redirect'], user_id=user_id, api_key_id=api_key_id)
        else:
            form = UserKeyForm(instance=key)

        context = {
            'key': key,
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['update_api_key']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the update_api_key view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
