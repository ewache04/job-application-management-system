# ManageJobApplications/forms/cover_letter_form/cover_letter_form.py
from django import forms
from ManageJobApplications.models import CoverLetter


class CoverLetterForm(forms.ModelForm):

    class Meta:
        model = CoverLetter
        fields = ['letter']
        placeholders = {
            'letter': 'Enter your cover letter',
        }
        labels = {
            'letter': 'Cover Letter',
        }
        widgets = {
            'letter': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 10, 'placeholder': placeholders['letter']}),
        }
