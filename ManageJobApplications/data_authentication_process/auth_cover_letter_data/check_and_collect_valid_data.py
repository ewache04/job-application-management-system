# ManageJobApplications/data_authentication_process/application_data/check_and_collect_valid_data.py
from ManageJobApplications.data_authentication_process.auth_cover_letter_data.auth_cover_letter_assistant_observation import \
    is_cover_letter_assistant_observation_data_valid
from ManageJobApplications.data_authentication_process.auth_cover_letter_data.auth_cover_letter_message import \
    is_cover_letter_message_data_valid

from ManageJobApplications.data_authentication_process.auth_cover_letter_data.auth_cover_letter_subject import \
    is_cover_letter_subject_data_valid


def check_and_collect_valid_data(cover_letter_data):
    valid_data, invalid_data = {}, {}

    # Validate cover letter subject
    if is_cover_letter_subject_data_valid(cover_letter_data):
        valid_data['subject'] = cover_letter_data.get('subject')
    else:
        invalid_data['subject'] = cover_letter_data.get('subject')

    # Validate cover letter
    if is_cover_letter_assistant_observation_data_valid(cover_letter_data):
        valid_data['assistant_observation'] = cover_letter_data.get('assistant_observation')
    else:
        invalid_data['assistant_observation'] = cover_letter_data.get('assistant_observation')

    # Validate cover letter
    if is_cover_letter_message_data_valid(cover_letter_data):
        valid_data['letter'] = cover_letter_data.get('letter')
    else:
        invalid_data['letter'] = cover_letter_data.get('letter')

    return valid_data, invalid_data
