# ManageJobApplications/data_authentication_process/application_data/auth_contact_person_data/auth_contact_person_email.py
def is_contact_person_email_data_valid(application_data):
    if 'contact_person_email' in application_data:
        contact_person_email = application_data.get('contact_person_email')
        if contact_person_email:
            return contact_person_email
        else:
            return None
    else:
        return None
