from django.http import request

from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_application_deadline import \
    is_application_deadline_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_company_name import \
    is_company_name_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_job_id import \
    is_job_id_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_job_posting_summary import \
    is_job_posting_summary_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_job_posting_urls import \
    is_job_posting_urls_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_job_title import \
    is_job_title_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_location import \
    is_location_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_contact_person_data.auth_contact_person_email import \
    is_contact_person_email_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_contact_person_data.auth_contact_person_first_name import \
    is_contact_person_first_name_data_valid

from ManageJobApplications.data_authentication_process.application_data.auth_contact_person_data.auth_contact_person_last_name import \
    is_contact_person_last_name_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_contact_person_data.auth_contact_person_notes import \
    is_contact_person_notes_data_valid
from ManageJobApplications.data_authentication_process.application_data.auth_contact_person_data.auth_contact_person_phone_number import \
    is_contact_person_phone_number_data_valid


def check_and_collect_valid_data(application_data):
    valid_data, invalid_data = {}, {}

    try:
        valid_deadline = is_application_deadline_data_valid(application_data)
        if valid_deadline:
            valid_data['application_deadline'] = valid_deadline
        else:
            invalid_data['application_deadline'] = valid_deadline
    except Exception as e:
        print(f"Error in validating application deadline: {e}")
        invalid_data['application_deadline'] = None

    try:
        valid_company_name = is_company_name_data_valid(application_data)
        if valid_company_name:
            valid_data['company_name'] = valid_company_name
        else:
            invalid_data['company_name'] = valid_company_name
    except Exception as e:
        print(f"Error in validating company name: {e}")
        invalid_data['company_name'] = None

    try:
        valid_job_posting_urls = is_job_posting_urls_data_valid(application_data)
        if valid_job_posting_urls:
            valid_data['job_posting_urls'] = valid_job_posting_urls
        else:
            invalid_data['job_posting_urls'] = None
    except Exception as e:
        print(f"Error in validating job posting URLs: {e}")
        invalid_data['job_posting_urls'] = None

    try:
        valid_location = is_location_data_valid(application_data)
        if valid_location:
            valid_data['location'] = valid_location
        else:
            invalid_data['location'] = valid_location
    except Exception as e:
        print(f"Error in validating location: {e}")
        invalid_data['location'] = None

    try:
        valid_job_id = is_job_id_data_valid(application_data)
        if valid_job_id:
            valid_data['job_id'] = valid_job_id
        else:
            invalid_data['job_id'] = valid_job_id
    except Exception as e:
        print(f"Error in validating job id: {e}")
        invalid_data['job_id'] = None

    try:
        valid_job_title = is_job_title_data_valid(application_data)
        if valid_job_title:
            valid_data['job_title'] = valid_job_title
        else:
            invalid_data['job_title'] = valid_job_title
    except Exception as e:
        print(f"Error in validating job title: {e}")
        invalid_data['job_title'] = None

    try:
        valid_job_posting_summary = is_job_posting_summary_data_valid(application_data)
        if valid_job_posting_summary:
            valid_data['job_posting_summary'] = valid_job_posting_summary
        else:
            invalid_data['job_posting_summary'] = valid_job_posting_summary
    except Exception as e:
        print(f"Error in validating job posting summary: {e}")
        invalid_data['job_posting_summary'] = None

    try:
        valid_contact_person_first_name = is_contact_person_first_name_data_valid(application_data)
        if valid_contact_person_first_name:
            valid_data['contact_person_first_name'] = valid_contact_person_first_name
        else:
            invalid_data['contact_person_first_name'] = valid_contact_person_first_name
    except Exception as e:
        print(f"Error in validating contact person first name: {e}")
        invalid_data['contact_person_first_name'] = None

    try:
        valid_contact_person_last_name = is_contact_person_last_name_data_valid(application_data)
        if valid_contact_person_last_name:
            valid_data['contact_person_last_name'] = valid_contact_person_last_name
        else:
            invalid_data['contact_person_last_name'] = valid_contact_person_last_name
    except Exception as e:
        print(f"Error in validating contact person last name: {e}")
        invalid_data['contact_person_last_name'] = None

    try:
        valid_contact_person_email = is_contact_person_email_data_valid(application_data)
        if valid_contact_person_email:
            valid_data['contact_person_email'] = valid_contact_person_email
        else:
            invalid_data['contact_person_email'] = valid_contact_person_email
    except Exception as e:
        print(f"Error in validating contact person email: {e}")
        invalid_data['contact_person_email'] = None

    try:
        valid_contact_person_phone_number = is_contact_person_phone_number_data_valid(application_data)
        if valid_contact_person_phone_number:
            valid_data['contact_person_phone_number'] = valid_contact_person_phone_number
        else:
            invalid_data['contact_person_phone_number'] = valid_contact_person_phone_number
    except Exception as e:
        print(f"Error in validating contact person phone number: {e}")
        invalid_data['contact_person_phone_number'] = None

    try:
        valid_contact_person_note = is_contact_person_notes_data_valid(application_data)
        if valid_contact_person_note:
            valid_data['contact_person_note'] = valid_contact_person_note
        else:
            invalid_data['contact_person_note'] = valid_contact_person_note
    except Exception as e:
        print(f"Error in validating contact person note: {e}")
        invalid_data['contact_person_note'] = None

    print('Checking and collecting valid data process: Passed!')
    return valid_data, invalid_data


# Example usage
# if __name__ == "__main__":
#     data = example_data_for_check_and_collect_valid_data()
#     validated_data = check_and_collect_valid_data(data)
#     print(type(validated_data))
#     print(validated_data)
