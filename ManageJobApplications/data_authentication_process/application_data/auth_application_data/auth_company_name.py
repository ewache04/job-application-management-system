# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_company_name.py
def is_company_name_data_valid(application_data):
    if 'company_name' in application_data:
        company_name = application_data.get('company_name')
        if company_name:
            return company_name
        else:
            return None
    else:
        return None
