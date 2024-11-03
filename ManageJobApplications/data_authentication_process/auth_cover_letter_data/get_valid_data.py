from ManageJobApplications.data_authentication_process.auth_cover_letter_data.check_and_collect_valid_data import \
    check_and_collect_valid_data
from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_cover_letter_data(cover_letter_data):
    valid_data, invalid_data = check_and_collect_valid_data(cover_letter_data)

    print(f'Valid Cover Letter Info: {valid_data.keys()}')
    get_horizontal_line()

    return valid_data
