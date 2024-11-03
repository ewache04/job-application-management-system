# ManageJobApplications/data_authentication_process/auth_interview_preparation_data/get_valid_data.py
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.check_and_collect_valid_data import \
    check_and_collect_valid_data
from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_interview_prep_data(interview_preparation_data):
    valid_data, invalid_data = check_and_collect_valid_data(interview_preparation_data)

    print(f'Valid interview preparation Info: {valid_data.keys()}')
    get_horizontal_line()

    return valid_data
