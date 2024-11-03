# ManageAccounts/views/logout_view/logout_view.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.greeting_message import greeting_user
from return_to_previous_page import return_to_previous_page


def login_view(request):
    user = request.user
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                print(f"Logged in as {user.email}")

                greeting = greeting_user(True, user.first_name)

                create_or_update_session(request, 'greeting_message', greeting)
                create_or_update_session(request, 'alert_message', 'You have been successfully logged in.')

                return redirect(urls_paths['user_home']['redirect'], user_id=user.pk)
    else:
        form = AuthenticationForm()
    context = {
        'urls_paths': urls_paths,
        'user': user,
        'form': form,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['login']['render'], context)
