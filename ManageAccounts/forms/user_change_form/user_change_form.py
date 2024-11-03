# ManageAccounts/forms/user_change_form/user_change_form.py

# Update user profile
from django import forms
from django.contrib.auth.forms import UserChangeForm
from ManageAccounts.models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']

        placeholders = {
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
            'username': 'Enter username',
            'email': 'Enter email address',
            'phone_number': 'Enter phone number',
        }

        labels = {
            'phone_number': 'Phone Number',
        }

        widgets = {
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': placeholders['phone_number']}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove the "No password set" message and the explanation
        self.fields['password'].help_text = None
