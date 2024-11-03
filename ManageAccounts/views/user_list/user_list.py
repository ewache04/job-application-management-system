# List all users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ManageAccounts.models import CustomUser
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def user_list(request):
    users = CustomUser.objects.all()
    context = {
        'urls_paths': urls_paths,
        'user': request.user,
        'users': users,
        'list_display_mode': True,
        'return_to_previous_page': return_to_previous_page,

    }
    return render(request, urls_paths['user_list']['render'], context)
