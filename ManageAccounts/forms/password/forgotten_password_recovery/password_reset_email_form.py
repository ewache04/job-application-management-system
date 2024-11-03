# ManageAccounts/forms/password/forgotten_password_recovery/password_reset_email_form.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm


class CustomPasswordResetForm(PasswordResetForm):
    """
    A custom form for password reset that includes email validation.

    This form inherits from Django's PasswordResetForm and overrides the email field
    to include custom styling and placeholder. It also includes a custom validation
    to check if the provided email is associated with an existing user.
    """

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        }),
        label='Email',
    )

    def clean_email(self):
        """
        Validate that the email is associated with an existing user.

        Returns:
            str: The cleaned email data.

        Raises:
            forms.ValidationError: If the email is not associated with any user.
        """
        email = self.cleaned_data.get('email')
        if not get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address.")
        return email
