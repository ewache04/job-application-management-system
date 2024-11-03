# ManageAccounts/views/password/forgotten_password_recovery/password_reset_confirm.py

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.forms import SetPasswordForm
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


def password_reset_confirm(request, uidb64=None, token=None):
    user_model = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user_model.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect(urls_paths['password_reset_complete']['redirect'])
        else:
            form = SetPasswordForm(user)
    else:
        form = None

    context = {
        'form': form,
        'urls_paths': urls_paths,
        'return_to_previous_page': return_to_previous_page,
        'uidb64': uidb64,
        'token': token,
    }
    return render(request, urls_paths['password_reset_confirm']['render'], context)
