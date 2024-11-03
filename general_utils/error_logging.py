# general_utils/error_logging.py

import logging


def log_error(message):
    """
    Log error messages to a file named 'error.log'.
    """
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(message)
