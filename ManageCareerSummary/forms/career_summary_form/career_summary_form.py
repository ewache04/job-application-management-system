# ManageCareerSummary/forms/career_summary_form/career_summary_form.py

from django import forms
from ManageCareerSummary.models import MyCareerSummary


class CareerSummaryForm(forms.ModelForm):
    class Meta:
        model = MyCareerSummary
        fields = ['career_summary']
