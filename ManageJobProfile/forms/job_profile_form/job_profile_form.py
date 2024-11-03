# ManageJobProfile/forms/job_profile_form/job_profile_form.py
from django import forms

from ManageJobProfile.models import JobProfile


class JobProfileForm(forms.ModelForm):
    class Meta:
        model = JobProfile
        fields = [
            'title',
            'company',
            'job_type',  # Include job_type field
            'start_date',
            'end_date',
            'description',
        ]
        labels = {
            'title': 'Your Job Title',
            'company': 'Company Name',
            'job_type': 'Job Type',  # Label for job_type field
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'description': 'Description of Role',
        }
        placeholders = {
            'title': 'Enter your job title',
            'company': 'Enter the company name',
            'job_type': 'Select the job type',
            'start_date': 'Select the start date',
            'end_date': 'Select the end date',
            'description': 'Provide a description of your role (e.g., responsibilities, qualifications)',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Software Engineer' or placeholders['title']}),
            'company': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Google Inc.' or placeholders['company']}),
            'job_type': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Full-time' or placeholders['job_type']}),
            # Widget for job_type field
            'start_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'May 24, 2020' or placeholders['start_date']}),
            'end_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'June 23, 2024' or placeholders['end_date']}),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'rows': 4, 'placeholder': 'Build and maintain softwares' or placeholders['description']}),
        }
