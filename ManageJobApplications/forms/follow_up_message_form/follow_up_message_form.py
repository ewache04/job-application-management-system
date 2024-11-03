# ManageJobApplications/forms/follow_up_message_form/follow_up_message_form.py

from django import forms
from ManageJobApplications.models import FollowUpMessage


class FollowUpMessageForm(forms.ModelForm):
    class Meta:
        model = FollowUpMessage
        fields = ['receivers_email', 'follow_up_message_subject', 'scheduled_send_date', 'follow_up_message']

        labels = {
            'receivers_email': 'Receiver\'s Email',
            'follow_up_message_subject': 'Follow-up Message Subject',
            'scheduled_send_date': 'Scheduled Send Date',
            'follow_up_message': 'Follow-up Message',

        }

        placeholders = {
            'receivers_email': 'Enter the email address of the recipient',
            'follow_up_message_subject': 'Enter the subject of the follow-up message',
            'scheduled_send_date': 'Select the date and time to schedule the follow-up message',
            'follow_up_message': 'Enter the content of the follow-up message',

        }

        widgets = {
            'receivers_email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['receivers_email']}),
            'follow_up_message_subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['follow_up_message_subject']}),
            'scheduled_send_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local',
                                                              'placeholder': placeholders['scheduled_send_date']}),
            'follow_up_message': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': placeholders['follow_up_message']}),

        }
