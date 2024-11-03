# ManageJobApplications/data_authentication_process/application_data/auth_cover_letter_subject.py

def is_cover_letter_subject_data_valid(cover_letter_data):
    if 'subject' in cover_letter_data:
        subject = cover_letter_data.get('subject')
        if subject:
            return subject
        else:
            return None
    else:
        return None

