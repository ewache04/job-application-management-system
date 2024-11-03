# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_job_posting_summary.py
def is_job_posting_summary_data_valid(application_data):
    if 'job_posting_summary' in application_data:
        job_posting_summary = application_data.get('job_posting_summary')
        if job_posting_summary:
            return job_posting_summary
        else:
            return None
    else:
        return None
