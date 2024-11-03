# ManageJobApplications/data_authentication_process/auth_interview_preparation_data/check_and_collect_valid_data.py
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.auth_interview_prep_about_company import \
    is_about_company_data_valid
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.auth_interview_prep_question import \
    is_prep_question_data_valid
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.auth_interview_prep_title import \
    is_title_data_valid


def check_and_collect_valid_data(interview_preparation_data):
    valid_data, invalid_data = {}, {}

    # Validate title
    title = is_title_data_valid(interview_preparation_data)
    if title:
        valid_data['title'] = title
    else:
        invalid_data['title'] = interview_preparation_data.get('title')

    # Validate about company
    about_company = is_about_company_data_valid(interview_preparation_data)
    if about_company:
        valid_data['about_company'] = about_company
    else:
        invalid_data['about_company'] = interview_preparation_data.get('about_company')

    # Validate preparation questions
    prep_questions = is_prep_question_data_valid(interview_preparation_data)
    if prep_questions:
        valid_data['prep_questions'] = prep_questions
    else:
        invalid_data['prep_questions'] = interview_preparation_data.get('prep_questions')

    print(f"Valid Data: {valid_data}")
    print(f"Invalid Data: {invalid_data}")

    return valid_data, invalid_data
