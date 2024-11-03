# ManageJobApplications/data_authentication_process/application_data/auth_cover_letter.py

def is_cover_letter_message_data_valid(cover_letter_data):
    if 'letter' in cover_letter_data:
        letter = cover_letter_data.get('letter')
        if letter:
            return letter
        else:
            return None
    else:
        return None
