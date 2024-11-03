# ManageJobApplications/data_authentication_process/application_data/auth_contact_person_data/auth_contact_person_last_name.py
def is_contact_person_last_name_data_valid(application_data):
    if 'contact_person_last_name' in application_data:
        contact_person_last_name = application_data.get('contact_person_last_name')
        if contact_person_last_name:
            return contact_person_last_name
        else:
            return None
    else:
        return None
