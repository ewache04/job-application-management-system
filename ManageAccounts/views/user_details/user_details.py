# View user details
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from ManageAccounts.models import CustomUser
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def user_details(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    context = {
        'urls_paths': urls_paths,
        'user': user,
        'search_table': False,
        'content_details_mode': True,
        'user_details_mode': True,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['user_details']['render'], context)
