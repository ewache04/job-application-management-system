# ManageJobApplications/forms/application_progress_status_form/application_progress_status_form.py
from django import forms

from ManageJobApplications.models import ApplicationProgressStatus
from ManageJobApplications.utils.get_application_status import get_application_status
from ManageJobApplications.utils.get_interest_level import get_interest_level


class ApplicationProgressStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationProgressStatus
        fields = ['interest_level', 'application_status']
        placeholders = {
            'interest_level': 'Select the level of interest',
            'application_status': 'Select the application status',
        }
        labels = {
            'interest_level': 'Interest Level',
            'application_status': 'Application Status',
        }
        widgets = {
            'interest_level': forms.Select(choices=get_interest_level(), attrs={'class': 'form-control',
                                                                                'placeholder': placeholders[
                                                                                    'interest_level']}),
            'application_status': forms.Select(choices=get_application_status(), attrs={'class': 'form-control',
                                                                                        'placeholder': placeholders[
                                                                                            'application_status']}),
        }