from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_application_deadline import \
    convert_application_deadline
from ManageJobApplications.forms.job_application_form.job_application_form import JobApplicationForm
from ManageJobApplications.models import ApplicationProgressStatus, JobApplication
from ManageJobApplications.utils.get_application_status import get_application_status
from ManageJobApplications.utils.get_interest_level import get_interest_level
from ManageJobApplications.utils.get_job_type import get_job_type
from ManageJobApplications.utils.get_visa_sponsorship import get_visa_sponsorship
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_application(request, user_id, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)
        progress_status = ApplicationProgressStatus.objects.filter(application=application).first()

        if request.method == 'POST':
            form = JobApplicationForm(request.POST, instance=application)

            if form.is_valid():
                print("Form is valid")

                # Convert application deadline string
                application_deadline_str = request.POST.get('application_deadline')
                application.application_deadline = convert_application_deadline(application_deadline_str)
                form.save()
                print("Saved Job Application")

                # Update progress level
                if not progress_status:
                    ApplicationProgressStatus.objects.create(user=user,
                                                             application=application,
                                                             application_status='Pending',
                                                             interest_level='Medium')
                    print("Created new Job progress_status")
                else:
                    progress_status.save()

                create_or_update_session(request, 'alert_message',
                                         'Your Job Application has been updated successfully.')
                return redirect(urls_paths['application_details']['redirect'],
                                user_id=user.pk, application_id=application.pk)
            else:
                print("Form is not valid")
                print(form.errors)
        else:
            form = JobApplicationForm(instance=application)

        context = {
            'application': application,
            'form': form,
            'urls_paths': urls_paths,
            'user': user,
            'progress_status': progress_status,
            'visa_sponsorship': get_visa_sponsorship(),
            'interest_level': get_interest_level(),
            'job_type': get_job_type(),
            'application_status': get_application_status(),
            'return_to_previous_page': return_to_previous_page,
        }
        return render(request, urls_paths['update_application']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the update_application view: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
