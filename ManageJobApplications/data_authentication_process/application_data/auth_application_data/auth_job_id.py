# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_job_id.py
def is_job_id_data_valid(application_data):
    if 'job_id' in application_data:
        job_id = application_data.get('job_id')
        if job_id:
            return job_id
        else:
            return None
    else:
        return None
