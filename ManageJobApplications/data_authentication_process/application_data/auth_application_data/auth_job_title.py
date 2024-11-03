# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_job_title.py
def is_job_title_data_valid(application_data):
    if 'job_title' in application_data:
        job_title = application_data.get('job_title')
        if job_title:
            return job_title
        else:
            return None
    else:
        return None
