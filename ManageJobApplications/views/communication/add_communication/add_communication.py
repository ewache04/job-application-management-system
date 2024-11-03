# ManageJobApplications/views/communication/add_communication/add_communication.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import JobApplication
from ManageJobApplications.views.communication.add_communication.generate_and_save_communication_message import \
    generate_and_save_communication_message
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from openai_tools.initialize_openai_client import get_openai_client
from return_to_previous_page import return_to_previous_page


@login_required
def add_communication(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        if request.method == 'POST':
            company_message = request.POST.get('company_message')
            applicant_message = request.POST.get('applicant_message')

            if company_message and applicant_message:
                # Get OpenAI client for the user
                client = get_openai_client(user)

                if client:
                    # Generate and save Follow-up Message
                    communication = generate_and_save_communication_message(
                        request,
                        client,
                        user,
                        application,
                        company_message,
                        applicant_message
                    )

                    if communication:
                        print('\nCommunication summary message saved (Auto)')

                        create_or_update_session(request, 'alert_message',
                                                 'Your Job Application Communication has been added successfully.')

                        return redirect(urls_paths['communication_details']['redirect'],
                                        application_id=application.pk, communication_id=communication.pk)
                    else:
                        print('\nFailed to generate communication message.')

        context = {
            'user': user,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['add_communication']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
