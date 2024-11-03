from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

from ManageCareerSummary.views.generate_career_summary.get_or_create_career_summary import get_or_create_career_summary
from ManageJobApplications.forms.follow_up_message_form.follow_up_message_form import FollowUpMessageForm
from ManageJobApplications.models import JobApplication, Resume, FollowUpMessage
from ManageJobApplications.views.follow_up_message.add_follow_up_message.generate_and_save_follow_up_message import \
    generate_and_save_follow_up_message
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from openai_tools.initialize_openai_client import get_openai_client
from return_to_previous_page import return_to_previous_page


@login_required
def add_follow_up_message(request, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)
        last_follow_up_message = FollowUpMessage.objects.filter(application=application).order_by('id').last()

        # Get or create the career summary
        career_summary = get_or_create_career_summary(request, user)

        try:
            resume = Resume.objects.get(application=application)
        except Resume.DoesNotExist:
            resume = None

        if request.method == 'POST':
            form = FollowUpMessageForm(request.POST)
            if form.is_valid():
                new_follow_up_message = form.cleaned_data.get("follow_up_message")
                client = get_openai_client(user)

                if client:
                    follow_up_message = generate_and_save_follow_up_message(client, user,
                                                                            application, career_summary,
                                                                            resume, last_follow_up_message,
                                                                            new_follow_up_message)

                    if follow_up_message:
                        print(f'Follow-up message was saved successfully')

                        create_or_update_session(request, 'alert_message',
                                                 'Your follow-up message has been created successfully.')
                        return redirect(urls_paths['follow_up_message_details']['redirect'],
                                        application_id=application.pk, follow_up_message_id=follow_up_message.pk)
                    else:
                        print("Follow-up message was not saved")
                        create_or_update_session(request, 'alert_message', 'Failed to save follow-up message.')
                else:
                    log_error("OpenAI client is not available. Please make sure API key is correct.")
                    create_or_update_session(request, 'alert_message',
                                             'OpenAI client is not available. Please make sure API key is correct.')
                    return redirect(urls_paths['add_api_key']['redirect'])
        else:
            form = FollowUpMessageForm()

        context = {
            'user': user,
            'form': form,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['add_follow_up_message']['render'], context)

    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")