from django.db import IntegrityError
from ManageJobApplications.models import Contact
from general_utils.error_logging import log_error


def save_contact_person(application, user, valid_contact_person_data):
    """
    Save contact person data for the given application and user if the data is valid.

    Parameters:
    - application: The application to which the contact person belongs.
    - user: The user who owns the contact person data.
    - valid_contact_person_data: A dictionary containing the validated contact person data.

    Returns:
    - The created Contact object if successful, None otherwise.
    """
    try:
        email = valid_contact_person_data.get('email')
        phone = valid_contact_person_data.get('phone')

        if email is not None or phone is not None:
            contact = Contact.objects.create(application=application, user=user, **valid_contact_person_data)
            print('Contact Person saved')
            return contact
        else:
            print('Contact Person was not saved')
    except IntegrityError as e:
        log_error(f"Integrity error while creating Contact: {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error while creating Contact: {str(e)}")

    return None
