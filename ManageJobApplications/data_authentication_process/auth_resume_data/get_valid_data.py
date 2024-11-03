from ManageJobApplications.data_authentication_process.auth_resume_data.check_and_collect_valid_data import \
    check_and_collect_valid_data
from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_resume_data(cover_letter_data):
    valid_data, invalid_data = check_and_collect_valid_data(cover_letter_data)

    print(f'Valid resume Info: {valid_data.keys()}')
    get_horizontal_line()

    return valid_data
