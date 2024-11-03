# ManageJobProfile/forms/job_profile_projects_form/job_profile_project_form.py

from django import forms
from django.forms import ModelForm

from ManageJobProfile.models import JobProfileProject


class JobProfileProjectForm(ModelForm):
    class Meta:
        model = JobProfileProject
        fields = ['project_subject', 'project_summary']

        labels = {
            'project_subject': 'Project Subject',
            'project_summary': 'Project Summary',
        }

        widgets = {
            'project_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project subject'}),
            'project_summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter project summary'}),
        }

