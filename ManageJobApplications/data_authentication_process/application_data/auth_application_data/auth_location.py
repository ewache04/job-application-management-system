# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_location.py
def is_location_data_valid(application_data):
    if 'location' in application_data:
        location = application_data.get('location')
        if location:
            return location
        else:
            return None
    else:
        return None



