# ManageJobApplications/forms/contact_form/contact_form.py

from django import forms
from ManageJobApplications.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'notes']
        placeholders = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Enter your email address',
            'phone_number': 'Enter your phone number',
            'notes': 'Enter any additional notes (if applicable)',
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'job_title': 'Job Title',
            'phone_number': 'Phone Number',
            'notes': 'Notes',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['first_name']}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': placeholders['last_name']}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': placeholders['email']}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['phone_number']}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': placeholders['notes']}),
        }
