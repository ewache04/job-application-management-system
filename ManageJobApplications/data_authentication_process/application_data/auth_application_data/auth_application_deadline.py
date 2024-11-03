from django.utils import timezone
from datetime import datetime

from ManageJobApplications.data_authentication_process.application_data.auth_application_data.test_data import test_data


def is_application_deadline_data_valid(application_data):
    """
    Check if the application deadline in the application data is valid.

    Parameters:
    - application_data (dict): A dictionary containing application details.

    Returns:
    - str or None: Valid date string if the application deadline is valid, None otherwise.
    """

    if 'application_deadline' in application_data:
        application_deadline = application_data.get('application_deadline')
        if application_deadline:
            try:
                # Convert application_deadline to timezone-aware date
                valid_deadline = timezone.datetime.strptime(application_deadline, '%Y-%m-%d').date()
                return valid_deadline.strftime('%Y-%m-%d')  # Return valid date
            except ValueError:
                # Handle invalid date format
                return None
    return None  # Return None if application_deadline is not in application_data or None


def convert_application_deadline(application_deadline_str):
    """
    Convert the application deadline string to a Python date object.

    Parameters:
    - application_deadline_str (str): The application deadline as a string.

    Returns:
    - date or None: Python date object if conversion is successful, None otherwise.
    """
    try:
        if application_deadline_str:
            # Convert the string to a Python date object
            application_deadline = datetime.strptime(application_deadline_str, '%Y-%m-%d')
            return application_deadline.date()
    except Exception as e:
        print(f"Error converting application deadline: {e}")
    return None


# Example dataset
# application_data = test_data()

# Validate the application deadline
# valid_deadline = is_application_deadline_data_valid(application_data)
# if valid_deadline:
#     print(f"Valid application deadline: {valid_deadline}")
# else:
#     print("Invalid or missing application deadline.")

# Convert the application deadline string to a Python date object
# application_deadline_str = application_data.get('application_deadline')
# converted_deadline = convert_application_deadline(application_deadline_str)
# if converted_deadline:
#     print(f"Converted application deadline: {converted_deadline}")
# else:
#     print("Error converting application deadline.")
