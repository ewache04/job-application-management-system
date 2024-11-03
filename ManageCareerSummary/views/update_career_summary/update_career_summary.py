# ManageCareerSummary/views/update_career_summary/update_career_summary.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render, get_object_or_404

from ManageCareerSummary.forms.career_summary_form.career_summary_form import CareerSummaryForm
from ManageCareerSummary.models import MyCareerSummary
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def update_career_summary(request, user_id, career_summary_id):
    try:
        user = request.user

        # Ensure career_summary_id is valid
        career_summary = get_object_or_404(MyCareerSummary, pk=career_summary_id, user=user)

        if request.method == 'POST':
            form = CareerSummaryForm(request.POST, instance=career_summary)
            if form.is_valid():
                form.instance.user = user
                career_summary = form.save()

                create_or_update_session(request, 'alert_message', 'Your career summary has been updated successfully.')

                return redirect(urls_paths['career_summary_details']['redirect'],
                                user_id=user.pk, career_summary_id=career_summary.pk)
        else:
            form = CareerSummaryForm(instance=career_summary)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'career_summary': career_summary,
            'form': form,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['update_career_summary']['render'], context)
    except Exception as e:
        log_error(f"An error occurred in the update_career_summary view: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
