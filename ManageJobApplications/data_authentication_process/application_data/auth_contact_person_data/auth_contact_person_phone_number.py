# ManageJobApplications/data_authentication_process/application_data/auth_contact_person_data/auth_contact_person_phone_number.py
def is_contact_person_phone_number_data_valid(application_data):
    if 'contact_person_phone_number' in application_data:
        contact_person_phone_number = application_data.get('contact_person_phone_number')
        if contact_person_phone_number:
            return contact_person_phone_number
        else:
            return None
    else:
        return None