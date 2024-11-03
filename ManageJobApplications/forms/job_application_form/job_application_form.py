# ManageJobApplications/forms/job_application_form/job_application_form.py
from django import forms

from ManageJobApplications.models import JobApplication
from ManageJobApplications.utils.get_job_type import get_job_type
from ManageJobApplications.utils.get_visa_sponsorship import get_visa_sponsorship


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'job_title', 'job_id', 'application_deadline', 'job_type',
                  'job_posting_urls', 'location', 'visa_sponsorship', 'job_posting_summary']
        labels = {
            'job_title': 'Job Title',
            'job_id': 'Job ID',
            'company_name': 'Company Name',
            'application_deadline': 'Application Deadline',
            'job_type': 'Job Type',
            'job_posting_urls': 'Job Posting URLs',
            'location': 'Location',
            'visa_sponsorship': 'Visa Sponsorship',
            'job_posting_summary': 'Job Posting Summary',
        }
        placeholders = {
            'job_title': 'Enter the job title',
            'job_id': 'Enter the job ID',
            'company_name': 'Enter the company name',
            'application_deadline': 'Select the application deadline',
            'job_posting_urls': 'Enter the job posting URLs',
            'location': 'Enter the job location',
            'job_posting_summary': 'Enter job posting summary',
        }

        widgets = {
            'application_deadline': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': placeholders['application_deadline']}),
            'visa_sponsorship': forms.Select(choices=get_visa_sponsorship(), attrs={'class': 'form-control'}),
            'job_type': forms.Select(choices=get_job_type(), attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['job_title']}),
            'job_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['job_id']}),
            'company_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['company_name']}),
            'job_posting_urls': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['job_posting_urls']}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['location']}),
            'job_posting_summary': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': placeholders['job_posting_summary']}),
        }
