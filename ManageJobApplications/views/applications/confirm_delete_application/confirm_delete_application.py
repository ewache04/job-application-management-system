from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from ManageJobApplications.models import JobApplication
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def confirm_delete_application(request, user_id, application_id):
    try:
        user = request.user
        application = get_object_or_404(JobApplication, pk=application_id, user=user)

        if request.method == 'POST':

            application.delete()

            # Update session with a success message
            create_or_update_session(request, 'alert_message', 'Your Job Application has been deleted successfully.')

            # Redirect to the application list page after deletion
            return redirect(urls_paths['application_list']['redirect'],
                            user_id=user.pk)

        # Context for the GET request
        context = {
            'user': user,
            'application': application,
            'urls_paths': urls_paths,
            'return_to_previous_page': return_to_previous_page,
        }

        # Render the confirmation page
        return render(request, urls_paths['confirm_delete_application']['render'], context)

    except Exception as e:
        log_error(f"An error occurred in confirm_delete_application view for user {request.user.id}: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
