# ManageAccounts/forms/password_change_form/password_change_form.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from ManageAccounts.models import CustomUser


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Custom form for changing the password of a CustomUser. Extends the built-in PasswordChangeForm
    to include custom placeholders, labels, and widgets for form fields.
    """
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']

        placeholders = {
            'old_password': 'Enter current password',
            'new_password1': 'Enter new password',
            'new_password2': 'Confirm new password',
        }

        labels = {
            'old_password': 'Current Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm New Password',
        }

        widgets = {
            'old_password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['old_password']}),
            'new_password1': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['new_password1']}),
            'new_password2': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['new_password2']}),
        }
