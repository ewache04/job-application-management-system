# ManageAccounts/forms/user_creation_form/user_creation_form.py

# Create a new user
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ManageAccounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        placeholders = {
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
            'username': 'Enter username',
            'email': 'Enter email address',
            'password1': 'Enter password',
            'password2': 'Confirm password',
        }
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': placeholders['password1']}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': placeholders['password2']}),
        }