from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ManageJobApplications.models import JobApplication, ApplicationCredential
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def application_credential_details(request, application_id, credential_id):
    try:
        user = request.user

        # Fetch the JobApplication object
        application = get_object_or_404(JobApplication, user=user, pk=application_id)
        print(f"Fetched JobApplication: {application}")

        # Fetch the ApplicationCredential object
        try:
            credential = get_object_or_404(ApplicationCredential, application=application)
            print(f"Fetched ApplicationCredential: {credential}")
        except Http404 as e:
            log_error(f"ApplicationCredential not found for JobApplication with ID {application_id}: {str(e)}")
            return HttpResponseServerError(f"An error occurred. Please try again later. No ApplicationCredential "
                                           f"matches the given query for JobApplication ID {application_id}.")

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'application': application,
            'credential': credential,
            'search_table': False,
            'content_details_mode': True,
            'credentials_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['application_credential_details']['render'], context)
    except Http404 as e:
        log_error(f"JobApplication not found: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
    except Exception as e:
        log_error(f"An error occurred in the application_credential_details view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
