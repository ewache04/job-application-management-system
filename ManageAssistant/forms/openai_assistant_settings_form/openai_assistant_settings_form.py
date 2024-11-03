# ManageAssistant/forms/openai_assistant_settings_form/openai_assistant_settings_form.py

from django import forms

from ManageAssistant.models import OpenAIAssistantSettings


class OpenAIAssistantSettingsForm(forms.ModelForm):
    class Meta:
        model = OpenAIAssistantSettings

        fields = ['selected_model', 'max_tokens', 'temperature', 'top_p', 'frequency_penalty', 'presence_penalty']
        widgets = {
            'selected_model': forms.Select(attrs={'class': 'form-control'}),
            'max_tokens': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max tokens'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Temperature'}),
            'top_p': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Top p'}),
            'frequency_penalty': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Frequency Penalty'}),
            'presence_penalty': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Presence Penalty'}),
        }
