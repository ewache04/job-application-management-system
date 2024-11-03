# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_visa_sponsorship.py
def is_visa_sponsorship_data_valid(application_data):
    if 'visa_sponsorship' in application_data:
        visa_sponsorship = application_data.get('visa_sponsorship')
        if visa_sponsorship:
            return visa_sponsorship
        else:
            return None
    else:
        return None
