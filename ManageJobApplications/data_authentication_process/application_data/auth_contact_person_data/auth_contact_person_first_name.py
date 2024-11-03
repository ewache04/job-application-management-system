# ManageJobApplications/data_authentication_process/application_data/auth_contact_person_data/auth_contact_person_first_name.py
def is_contact_person_first_name_data_valid(application_data):
    if 'contact_person_first_name' in application_data:
        contact_person_first_name = application_data.get('contact_person_first_name')
        if contact_person_first_name:
            return contact_person_first_name
        else:
            return None
    else:
        return None