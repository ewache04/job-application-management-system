# ManageJobApplications/forms/resume_form/resume_form.py
from django import forms

from ManageJobApplications.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'assistant_resume',
        ]

        widgets = {
            'assistant_resume': forms.Textarea(attrs={'placeholder': 'Type or past resume content here......'}),
        }

        labels = {
            'assistant_resume': 'Enter Resume',
        }
