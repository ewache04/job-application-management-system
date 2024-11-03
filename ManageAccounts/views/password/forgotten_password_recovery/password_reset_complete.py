# ManageAccounts/views/password/forgotten_password_recovery/password_reset_complete.py
from django.shortcuts import render

from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


def password_reset_complete(request):

    context = {
        'urls_paths': urls_paths,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['password_reset_complete']['render'], context)
