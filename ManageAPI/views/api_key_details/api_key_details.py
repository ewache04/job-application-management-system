# jetbrains://pycharm/navigate/reference?project=OpenColabAI&path=ManageAPI/views/api_key_details/api_key_details.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from OpenColabAI.settings import urls_paths
from ManageAPI.models import UserKey
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def api_key_details(request, user_id, api_key_id):
    user = request.user
    try:
        api_key = get_object_or_404(UserKey, pk=api_key_id, user=user)

        context = {
            'api_key': api_key,
            'urls_paths': urls_paths,
            'user': user,
            'search_table': False,
            'content_details_mode': True,
            'api_key_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['api_key_details']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the api_key_details view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
