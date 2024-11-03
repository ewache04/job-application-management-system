# ManageBackgroundLooks/views/create_or_update_backgroundlooks.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from ManageBackgroundLooks.forms.backgroundlooks_form.backgroundlooks_form import BackgroundLooksForm
from ManageBackgroundLooks.models import MyBackgroundLooks
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def create_or_update_backgroundlooks(request, user_id, backgroundlooks_id=None):
    try:
        user = request.user

        if backgroundlooks_id:
            backgroundlooks_obj = MyBackgroundLooks.objects.get(pk=backgroundlooks_id, user=user)
        else:
            backgroundlooks_obj = MyBackgroundLooks(user=user)

        if request.method == 'POST':
            form = BackgroundLooksForm(request.POST, instance=backgroundlooks_obj)
            if form.is_valid():
                form.instance.user = user
                backgroundlooks = form.save()
                create_or_update_session(request, 'alert_message', 'Your background image has been successfully saved.')
                return redirect(urls_paths['user_home']['redirect'], user_id=user.pk)
        else:
            form = BackgroundLooksForm(instance=backgroundlooks_obj)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'backgroundlooks': backgroundlooks_obj,
            'form': form,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['create_or_update_backgroundlooks']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the create_or_update_backgroundlooks view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
