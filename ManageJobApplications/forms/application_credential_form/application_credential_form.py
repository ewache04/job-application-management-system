# ManageJobApplications/forms/application_credential_form/application_credential_form.py
from django import forms
from ManageJobApplications.models import ApplicationCredential


class ApplicationCredentialForm(forms.ModelForm):
    class Meta:
        model = ApplicationCredential
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username used for creating account with this company'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password used for creating account with this company'
            }),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
