# ManageJobApplications/forms/communication_form/communication_form.py
from django import forms

from ManageJobApplications.models import Communication


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ['communication_subject', 'communication_summary']
        widgets = {
            'communication_subject': forms.TextInput(attrs={
                'rows': 12,
                'class': 'form-control',
                'placeholder': 'Please provide the most recent message you received from the company (e.g., '
                               'confirmation of application received)'
            }),
            'communication_summary': forms.Textarea(attrs={
                'rows': 12,
                'class': 'form-control',
                'placeholder': 'Please provide your response to the company\'s message you provided'
            }),
        }
        labels = {
            'communication_subject': 'Communication Subject:',
            'communication_summary': 'Communication Summary:',
        }
