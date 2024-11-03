# ManageAccounts/views/payment_profile/payment_profile.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render

from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def payment_profile(request, user_id):
    user = request.user
    try:
        context = {
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['payment_profile']['render'], context)

    except Exception as e:
        log_error(f"An error occurred in the payment profile view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
