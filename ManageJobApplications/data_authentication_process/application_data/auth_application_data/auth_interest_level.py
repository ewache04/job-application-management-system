# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_interest_level.py
def is_interest_level_data_valid(application_data):
    if 'interest_level' in application_data:
        interest_level = application_data.get('interest_level')
        if interest_level:
            return interest_level
        else:
            return None
    else:
        return None
