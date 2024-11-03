# ManageBackgroundLooks/views/create_or_update_backgroundlooks/get_background_color.py
from django.core.exceptions import ObjectDoesNotExist
from ManageBackgroundLooks.models import MyBackgroundLooks
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

def set_selected_background(user, request):
    """
    Fetch the latest background look for the user and store the color in the session.

    Args:
        user (User): The user object.
        request (HttpRequest): The HTTP request object.

    Returns:
        str: The background color.
    """
    selected_background_color = 'white'  # Default value

    try:
        # Fetch the latest background look for the user
        selected_background = MyBackgroundLooks.objects.filter(user=user).order_by('created_at').last()
        if selected_background:
            # Extract the color or relevant attribute
            selected_background_color = selected_background.selected_background

    except ObjectDoesNotExist:
        pass  # Use the default 'white'
    finally:
        # Store the background color in the session
        create_or_update_session(request, 'selected_background', selected_background_color)
        print(f'selected_background_color: {selected_background_color}')

    return selected_background_color
