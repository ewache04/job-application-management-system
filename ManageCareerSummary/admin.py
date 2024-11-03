# ManageCareerSummary/admin.py
from django.contrib import admin

from ManageCareerSummary.models import MyCareerSummary


# Register your models here.

class MyCareerSummaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'career_summary', 'user', 'created_at', 'updated_at']
    list_filter = ['id', 'created_at', 'updated_at']
    search_fields = ['id', 'created_at']


# Register MyCareerSummary model with admin site
admin.site.register(MyCareerSummary, MyCareerSummaryAdmin)
