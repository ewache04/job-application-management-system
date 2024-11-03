# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_application_status.py
def is_application_status_data_valid(application_data):
    if 'application_status' in application_data:
        application_status = application_data.get('application_status')
        if application_status:
            return application_status
        else:
            return None
    else:
        return None
