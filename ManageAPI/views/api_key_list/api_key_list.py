# jetbrains://pycharm/navigate/reference?project=OpenColabAI&path=ManageAPI/views/add_api_key/add_api_key.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render
from OpenColabAI.settings import urls_paths
from ManageAPI.models import UserKey
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def api_key_list(request, user_id=None):
    try:
        user = request.user
        api_keys = UserKey.objects.filter(user=user).order_by('id')

        context = {
            'api_keys': api_keys,
            'urls_paths': urls_paths,
            'user': user,
            'search_table': True,
            'list_display_mode': True,
            'api_key_list_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['api_key_list']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the api_key_list view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
