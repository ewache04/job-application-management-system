# Change user password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render

from ManageAccounts.models import CustomUser
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def change_password(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            create_or_update_session(request, 'alert_message', 'Your password has been successfully changed.')

            return redirect(urls_paths['user_home']['redirect'], user_id=user.pk)
    else:
        form = PasswordChangeForm(user=user)

    context = {
        'urls_paths': urls_paths,
        'user': user,
        'form': form,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['change_password']['render'], context)
