# ManageJobApplications/forms/interview_preparation_form/interview_preparation_form.py
from django import forms

from ManageJobApplications.models import InterviewPreparation


class InterviewPreparationForm(forms.ModelForm):
    class Meta:
        model = InterviewPreparation
        fields = ['about_company', 'prep_questions']
        widgets = {

            'about_company': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter about company'}),

            'prep_questions': forms.Textarea(attrs={'class': 'form-control',
                                                    'rows': 5, 'placeholder': 'Enter preparation question'}),
        }

        labels = {

            'about_company': 'About Company',
            'prep_questions': 'Preparation Question',
        }
