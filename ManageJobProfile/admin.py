# ManageJobApplications/admin.py
from django.contrib import admin

from ManageJobProfile.models import JobProfile, JobProfileProject


class JobProfileAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'company', 'job_type', 'start_date', 'end_date', 'description',
        'user')  # Include job_type in list display
    search_fields = ['title', 'company', 'description']
    list_filter = ['job_type', 'start_date', 'end_date', 'user']


class JobProfileProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_subject', 'user', 'created_at', 'updated_at']
    list_filter = ['user', 'project_subject', 'created_at', 'updated_at']
    search_fields = ['project_subject', 'project_summary']


# Register JobProfile model with admin site
admin.site.register(JobProfile, JobProfileAdmin)

# Register JobProfile model with admin site
admin.site.register(JobProfileProject, JobProfileProjectAdmin)
