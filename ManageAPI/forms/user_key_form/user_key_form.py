# ManageAPI/forms/user_key_form/user_key_form.py
from django import forms

from ManageAPI import key_names
from ManageAPI.models import UserKey


class UserKeyForm(forms.ModelForm):
    class Meta:
        model = UserKey
        fields = ['key_name', 'key_value', 'is_default']  # Include 'is_default' field in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['key_name'].widget = forms.Select(choices=key_names.key_names())
        self.fields['key_value'].widget.attrs['placeholder'] = 'Enter key value'
