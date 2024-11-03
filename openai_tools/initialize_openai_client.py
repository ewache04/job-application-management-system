# openai_tools/initialize_openai_client.py
from openai import OpenAI
from ManageAPI.models import UserKey


def get_openai_client(user=None):
    """
    Function to initialize and return OpenAI client with user's default API key.
    """
    # Assuming UserKey model has a field named is_default to indicate the default key
    # Assuming 'OPENAI_API_KEY' is the key_name for OpenAI API key
    default_key = UserKey.objects.filter(user=user, is_default=True, key_name='OPENAI_API_KEY').first()

    print('Default API key is', default_key)  # Comma added here

    if default_key:
        # Initialize OpenAI client with the default key value
        client = OpenAI(api_key=default_key.key_value)

        # Assuming create_or_update_session is a custom function to manage sessions
        # client = create_or_update_session(request, 'openai_client', client)

        return client
    else:
        # Handle case where user doesn't have a default key set or OpenAI key not found
        return None
