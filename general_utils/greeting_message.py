# general_utils/greeting_message.py
from datetime import datetime

# Get the current time
current_time = datetime.now().time()


def greeting_user(auth_status, first_name):
    # Determine the greeting message based on the current time and user's first_name
    if auth_status and first_name:
        if current_time.hour < 12:
            greeting_message = f'Good morning, {first_name}!'
        elif current_time.hour < 18:
            greeting_message = f'Good afternoon, {first_name}!'
        else:
            greeting_message = f'Good evening, {first_name}!'
    else:
        if current_time.hour < 12:
            greeting_message = 'Good morning!'
        elif current_time.hour < 18:
            greeting_message = 'Good afternoon!'
        else:
            greeting_message = 'Good evening!'

    return greeting_message
