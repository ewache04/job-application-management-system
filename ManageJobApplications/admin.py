# ManageJobApplications/admin.py
from django.contrib import admin

from .forms.application_progress_status_form.application_progress_status_form import ApplicationProgressStatusForm
from .forms.contact_form.contact_form import ContactForm
from .forms.cover_letter_form.cover_letter_form import CoverLetterForm
from .forms.follow_up_message_form.follow_up_message_form import FollowUpMessageForm
from .forms.job_application_form.job_application_form import JobApplicationForm
from .forms.resume_form.resume_form import ResumeForm
from .models import JobApplication, ApplicationProgressStatus, Contact, Communication, CoverLetter, Resume, \
    InterviewPreparation, FollowUpMessage, ApplicationCredential, Document


class JobApplicationAdmin(admin.ModelAdmin):
    form = JobApplicationForm
    list_display = ['company_name', 'job_title', 'job_id', 'application_deadline', 'job_type', 'location']
    list_filter = ['company_name', 'job_title', 'location']
    search_fields = ['company_name', 'job_title', 'location']
    date_hierarchy = 'application_deadline'

    fieldsets = (
        (None, {
            'fields': (
                'company_name', 'job_title', 'job_id', 'application_deadline', 'location', 'visa_sponsorship',
                'job_type',
            )
        }),
        ('Application Status', {
            'fields': ('application_status',)
        }),
    )


class ApplicationProgressAdmin(admin.ModelAdmin):
    form = ApplicationProgressStatusForm
    list_display = ('interest_level', 'application_status', 'created_at', 'updated_at')
    list_filter = ['interest_level', 'application_status', 'created_at', 'updated_at']
    search_fields = ['interest_level', 'application_status']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Application Status', {
            'fields': ('interest_level', 'application_status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number', 'notes']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class CommunicationsAdmin(admin.ModelAdmin):
    list_display = ['communication_subject', 'created_at', 'updated_at']
    search_fields = ['communication_subject', 'created_at']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class FollowUpMessagesAdmin(admin.ModelAdmin):
    form = FollowUpMessageForm
    list_display = ['receivers_email', 'follow_up_message_subject', 'scheduled_send_date', 'created_at', 'updated_at']
    search_fields = ['receivers_email', 'follow_up_message_subject']
    list_filter = ['scheduled_send_date', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class CoverLetterAdmin(admin.ModelAdmin):
    form = CoverLetterForm
    list_display = ['subject', 'created_at', 'updated_at']
    search_fields = ['subject', 'letter']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class ResumeAdmin(admin.ModelAdmin):
    form = ResumeForm
    list_display = ['resume_name', 'created_at', 'updated_at']
    search_fields = ['resume_name', 'resume_email', ]
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class InterviewPreparationAdmin(admin.ModelAdmin):
    list_display = ('application', 'user', 'title', 'created_at', 'updated_at')
    search_fields = ('application__company_name', 'user__username', 'title')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


class ApplicationCredentialAdmin(admin.ModelAdmin):
    list_display = ('user', 'application', 'username', 'created_at', 'updated_at')
    search_fields = ('user__username', 'application__job_title', 'username')
    list_filter = ('created_at', 'updated_at')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'user', 'document_type', 'file', 'uploaded_at')
    search_fields = ('application__job_title', 'user__username', 'document_type')
    list_filter = ('document_type', 'uploaded_at')
    ordering = ('-uploaded_at',)
    fieldsets = (
        (None, {
            'fields': ('application', 'user', 'document_type', 'file')
        }),
        ('Timestamps', {
            'fields': ('uploaded_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('uploaded_at',)


# Register JobApplication model with admin site
admin.site.register(JobApplication, JobApplicationAdmin)

# Register ApplicationProgressStatus model with admin site
admin.site.register(ApplicationProgressStatus, ApplicationProgressAdmin)

# Register Contact model with admin site
admin.site.register(Contact, ContactAdmin)

# Register Communications model with admin site
admin.site.register(Communication, CommunicationsAdmin)

# Register CoverLetter model with admin site
admin.site.register(CoverLetter, CoverLetterAdmin)

# Register Resume model with admin site
admin.site.register(Resume, ResumeAdmin)

# Register InterviewPreparationAdmin model with admin site
admin.site.register(InterviewPreparation, InterviewPreparationAdmin)

# Register FollowUpMessage model with admin site
admin.site.register(FollowUpMessage, FollowUpMessagesAdmin)

# Register Application Credentials model with admin site
admin.site.register(ApplicationCredential, ApplicationCredentialAdmin)

# Register Application Documents model with admin site
admin.site.register(Document, DocumentAdmin)
