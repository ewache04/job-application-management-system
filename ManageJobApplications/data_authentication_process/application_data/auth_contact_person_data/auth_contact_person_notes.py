# ManageJobApplications/data_authentication_process/application_data/auth_contact_person_data/auth_contact_person_notes.py
def is_contact_person_notes_data_valid(application_data):
    if 'contact_person_notes' in application_data:
        contact_person_notes = application_data.get('contact_person_notes')
        if contact_person_notes:
            return contact_person_notes
        else:
            return None
    else:
        return None