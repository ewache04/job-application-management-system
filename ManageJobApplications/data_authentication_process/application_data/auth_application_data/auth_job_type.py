# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_job_type.py
def is_job_type_data_valid(application_data):
    if 'job_type' in application_data:
        job_type = application_data.get('job_type')
        if job_type:
            return job_type
        else:
            return None
    else:
        return None
