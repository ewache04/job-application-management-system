# ManageBackgroundLooks/forms/backgroundlooks_form/backgroundlooks_form.py
from django import forms

from ManageBackgroundLooks.background_choices import background_choices
from ManageBackgroundLooks.models import MyBackgroundLooks


class BackgroundLooksForm(forms.ModelForm):
    class Meta:
        model = MyBackgroundLooks
        fields = ['selected_background']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['selected_background'].widget = forms.Select(choices=background_choices())
