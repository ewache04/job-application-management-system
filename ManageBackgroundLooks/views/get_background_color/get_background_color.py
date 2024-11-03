# ManageBackgroundLooks/views/create_or_update_backgroundlooks/get_background_color.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ManageBackgroundLooks.views.create_or_update_backgroundlooks.set_selected_background import set_selected_background


@login_required
def get_background_color(request, user_id):
    user = request.user
    selected_background = set_selected_background(user, request)
    return JsonResponse({'background_color': selected_background})
