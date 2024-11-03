from django.shortcuts import render

from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


def payment_cancelled(request, user_id):
    user = request.user

    context = {

        'urls_paths': urls_paths,
        'user': user,
        'return_to_previous_page': return_to_previous_page,
    }

    return render(request, urls_paths['payment_cancelled']['render'], context)
