# general_utils/get_env_variable.py
import os
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable")
