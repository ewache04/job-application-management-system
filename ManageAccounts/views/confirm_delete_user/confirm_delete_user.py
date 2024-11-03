# Delete user with confirmation
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ManageAccounts.models import CustomUser
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def confirm_delete_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        user.delete()
        create_or_update_session(request, 'alert_message', 'Your account has been successfully deleted.')

        return redirect(urls_paths['index']['redirect'])
    context = {
        'urls_paths': urls_paths,
        'user': request.user,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['confirm_delete_user']['render'], context)


