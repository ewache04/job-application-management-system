# Update user profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ManageAccounts.forms.user_change_form.user_change_form import CustomUserChangeForm
from ManageAccounts.models import CustomUser

from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def update_profile(request, user_id):

    user = get_object_or_404(CustomUser, pk=user_id)

    print(user)

    if request.method == 'POST':

        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            create_or_update_session(request, 'alert_message', 'Your profile has been successfully updated.')

            return redirect(urls_paths['user_details']['redirect'], user_id=user.pk)

    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'urls_paths': urls_paths,
        'user': user,
        'form': form,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['update_profile']['render'], context)
