
from ManageJobApplications.data_authentication_process.application_data.check_and_collect_valid_application_and_contact_person_data import \
    check_and_collect_valid_data

from general_utils.get_horizontal_line import get_horizontal_line


def get_valid_application_data(application_data):
    valid_data, invalid_data = check_and_collect_valid_data(application_data)

    # Exclude contact person information
    valid_data.pop('contact_person_first_name', None)
    valid_data.pop('contact_person_last_name', None)
    valid_data.pop('contact_person_email', None)
    valid_data.pop('contact_person_phone_number', None)
    valid_data.pop('contact_person_notes', None)
    valid_data.pop('interest_level', None)
    valid_data.pop('application_status', None)

    print(f'Valid Company Info: {valid_data.keys()}')
    get_horizontal_line()

    return valid_data


def get_valid_job_contact_person_info(application_data):
    # Create an empty dictionary to store valid contact person information
    valid_contact_person_info = {}

    # Check if the required keys exist in the application data
    if 'contact_person_first_name' in application_data:
        valid_contact_person_info['first_name'] = application_data['contact_person_first_name']

    if 'contact_person_last_name' in application_data:
        valid_contact_person_info['last_name'] = application_data['contact_person_last_name']

    if 'contact_person_email' in application_data:
        valid_contact_person_info['email'] = application_data['contact_person_email']

    if 'contact_person_phone_number' in application_data:
        valid_contact_person_info['phone_number'] = application_data['contact_person_phone_number']

    if 'contact_person_notes' in application_data:
        valid_contact_person_info['notes'] = application_data['contact_person_notes']

    print(f'Valid Contact Person Info: {valid_contact_person_info.keys()}')
    get_horizontal_line()

    return valid_contact_person_info


# application_data = test_data()
# get_valid_application_data(application_data)
# get_valid_job_contact_person_info(application_data)

# Example usage
# if __name__ == "__main__":
#     data = example_data_for_check_and_collect_valid_data()
#
#     validated_data = get_valid_application_data(data)
#     print(type(validated_data))
#     print(validated_data)
#
#     validated_data = get_valid_job_contact_person_info(data)
#     print(type(validated_data))
#     print(validated_data)
