# ManageAPI/views/confirm_delete_api_key/confirm_delete_api_key.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from OpenColabAI.settings import urls_paths
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from ManageAPI.models import UserKey
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def confirm_delete_api_key(request, user_id, api_key_id):
    user = request.user
    try:
        key = get_object_or_404(UserKey, pk=api_key_id, user=user)
        if request.method == 'POST':
            key.delete()
            create_or_update_session(request, 'alert_message', 'Your API Key has been deleted successfully.')
            return redirect(urls_paths['api_key_list']['redirect'], user_id=user_id)

        context = {
            'key': key,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['confirm_delete_api_key']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the confirm_delete_api_key view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
