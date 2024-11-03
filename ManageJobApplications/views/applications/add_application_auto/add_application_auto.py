# ManageJobApplications/views/applications/add_application_auto/add_application_auto.py

# Django imports
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
# ManageJobApplications imports
from ManageJobApplications.data_authentication_process.application_data.auth_application_data.auth_job_posting_urls import \
    is_valid_url
from ManageJobApplications.data_authentication_process.application_data.data_format_conversion.extract_application_data import \
    extract_application_data
from ManageJobApplications.data_authentication_process.application_data.get_valid_data import \
    get_valid_application_data, get_valid_job_contact_person_info
from ManageJobApplications.models import JobApplication
from ManageJobApplications.utils.get_application_status import get_application_status
from ManageJobApplications.utils.get_interest_level import get_interest_level
from ManageJobApplications.utils.get_job_type import get_job_type
from ManageJobApplications.utils.get_visa_sponsorship import get_visa_sponsorship
from ManageJobApplications.utils.resume.process_resume_file import process_resume_file
from ManageJobApplications.utils.thread_delay import thread_delay
from ManageJobApplications.views.application_progress_status.create_application_progress_status import (
    create_application_progress_status)
from ManageJobApplications.views.contacts.add_contact.save_contact_person import save_contact_person
from ManageJobApplications.views.cover_letter.add_cover_letter.generate_and_save_cover_letter import \
    generate_and_save_cover_letter
from ManageJobApplications.views.follow_up_message.add_follow_up_message.generate_and_save_follow_up_message import \
    generate_and_save_follow_up_message
from ManageJobApplications.views.interview_preparation.add_interview_preparation.generate_and_save_interview_preparation import \
    generate_and_save_interview_preparation

# OpenColabAI imports
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths

# General utilities imports
from general_utils.error_logging import log_error
from openai_tools.initialize_openai_client import get_openai_client
from return_to_previous_page import return_to_previous_page


@login_required
def add_application_auto(request, user_id=None):
    try:
        user = request.user

        if request.method == 'POST':
            job_posting_url = request.POST.get('job_posting_url').strip()
            application_description_without_url = request.POST.get('summarize_job_application').strip()
            application_description = application_description_without_url

            # Get or create the career summary
            career_summary = get_or_create_career_summary(request, user)

            raw_cover_letter = None

            raw_interview_preparation = None

            client = get_openai_client(user)

            if client:
                try:
                    application_data = extract_application_data(application_description, client)

                    if application_data:
                        valid_application_data = get_valid_application_data(application_data)

                        if valid_application_data:
                            application = JobApplication.objects.create(user=user, **valid_application_data)
                            print(f'\nApplication Saved {valid_application_data}')

                            create_application_progress_status(application, user, interest_level="Medium",
                                                               application_status="Pending")
                            print(f'\nApplication Progress Status Saved')

                            valid_contact_person_data = get_valid_job_contact_person_info(application_data)

                            if valid_contact_person_data:
                                save_contact_person(application, user, valid_contact_person_data)

                            thread_delay()
                            resume = process_resume_file(request, client, user, application, career_summary)

                            thread_delay()
                            generate_and_save_cover_letter(request, client, user, application,
                                                           career_summary, resume, raw_cover_letter)

                            thread_delay()
                            generate_and_save_follow_up_message(client, user,
                                                                application, career_summary,
                                                                resume)

                            thread_delay()
                            generate_and_save_interview_preparation(request,
                                                                    client, user,
                                                                    application,
                                                                    career_summary,
                                                                    raw_interview_preparation)

                            valid_url = is_valid_url(job_posting_url)
                            print(f"valid_url: {valid_url}")
                            if valid_url:
                                try:
                                    application.job_posting_urls = valid_url
                                    application.save(update_fields=['job_posting_urls'])
                                    print(f"Job posting URL saved: {application.job_posting_urls}")
                                except Exception as e:
                                    log_error(f"An error occurred while saving job posting URL: {str(e)}")
                                    return HttpResponseServerError(f"An error occurred while saving job posting URL. "
                                                                   f"Please try again later. {str(e)}")

                            create_or_update_session(request, 'alert_message', 'Your Job Application has been created '
                                                                               'successfully.')
                            return redirect(urls_paths['application_details']['redirect'],
                                            user_id=user.pk, application_id=application.pk)
                        else:
                            create_or_update_session(request, 'alert_message', 'Your Job Application could not be '
                                                                               'created successfully. Please check '
                                                                               'your input and try again.')
                            return redirect(urls_paths['add_application']['redirect'], user_id=user.pk)
                    else:
                        create_or_update_session(request, 'alert_message', 'Your Job Application could not be created '
                                                                           'successfully. Job description might be '
                                                                           'too long.')
                        return redirect(urls_paths['add_application']['redirect'])
                except Exception as e:
                    log_error(f"An error occurred in the add_application_auto view: {str(e)}")
                    return HttpResponseServerError("An error occurred. Please try again later.")
            else:
                log_error("OpenAI client is not available. Please make sure API key is correct.")
                create_or_update_session(request, 'alert_message', 'OpenAI client is not available. Please make sure '
                                                                   'API key is correct.')
                return redirect(urls_paths['add_api_key']['redirect'], user_id=user.pk)
        else:
            context = {
                'urls_paths': urls_paths,
                'user': user,
                'visa_sponsorship': get_visa_sponsorship(),
                'interest_level': get_interest_level(),
                'job_type': get_job_type(),
                'application_status': get_application_status(),
                'return_to_previous_page': return_to_previous_page,
            }
            return render(request, urls_paths['add_application_auto']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the add_application_auto view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later.{str(e)}")
