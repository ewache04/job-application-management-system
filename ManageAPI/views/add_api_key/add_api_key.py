# ManageAPI/templates/add_api_key.html
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from ManageAPI.forms.user_key_form.user_key_form import UserKeyForm
from ManageAPI.models import UserKey
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def add_api_key(request, user_id):
    try:
        user = request.user
        api_keys = UserKey.objects.filter(user=user).order_by('id')

        if request.method == 'POST':
            form = UserKeyForm(request.POST)

            if form.is_valid():
                key_value = form.cleaned_data['key_value']
                if api_keys.filter(key_value=key_value).exists():
                    create_or_update_session(request, 'alert_message', 'Your API Key already exists.')
                    existing_key = api_keys.filter(key_value=key_value).first()
                    return redirect(urls_paths['api_key_details']['redirect'], user_id=user.pk, api_key_id=existing_key.pk)

                api_key = form.save(commit=False)
                api_key.user = user
                api_key.save()

                create_or_update_session(request, 'alert_message', 'Your API Key has been created successfully.')
                return redirect(urls_paths['api_key_details']['redirect'], user_id=user.pk, api_key_id=api_key.pk)
        else:
            form = UserKeyForm()

        context = {
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['add_api_key']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the add_api_key view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")