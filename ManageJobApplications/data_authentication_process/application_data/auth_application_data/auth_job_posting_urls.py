# ManageJobApplications/data_authentication_process/application_data/auth_application_data/auth_job_posting_urls.py
from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.forms.fields import URLField

from general_utils.error_logging import log_error


def is_job_posting_urls_data_valid(application_data):
    if 'job_posting_urls' in application_data:
        job_posting_urls = application_data.get('job_posting_urls')
        if job_posting_urls:
            url_validator = URLField()
            try:
                # Validate the URL
                url_validator.clean(job_posting_urls)
                return job_posting_urls
            except ValidationError:
                return None
        else:
            return None
    else:
        return None


def is_valid_url(url):
    try:
        parsed_url = urlparse(url)
        return url if all([parsed_url.scheme, parsed_url.netloc]) else None
    except Exception as e:
        log_error(f"An error occurred while validating URL: {str(e)}")
        return None
