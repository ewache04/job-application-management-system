# ManageJobApplications/models.py
import os

from django.db import models
from django.conf import settings
from django.utils import timezone

from ManageJobApplications.utils.get_application_status import get_application_status
from ManageJobApplications.utils.get_interest_level import get_interest_level
from ManageJobApplications.utils.get_job_type import get_job_type
from ManageJobApplications.utils.get_visa_sponsorship import get_visa_sponsorship


class JobApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_posting_urls = models.URLField(max_length=1500, null=True, blank=True, verbose_name="Job Posting URLs")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    job_title = models.CharField(max_length=255, verbose_name="Job Title", blank=True)
    job_id = models.CharField(max_length=255, verbose_name="Job id", blank=True)
    location = models.CharField(max_length=255, verbose_name="Location", blank=True)
    job_posting_summary = models.TextField(max_length=3500, verbose_name="Application Description", blank=True,
                                           null=True)

    application_deadline = models.DateField(null=True, blank=True, verbose_name="Application Deadline")

    VISA_SPONSORSHIP = get_visa_sponsorship()
    visa_sponsorship = models.CharField(default=False, max_length=25,
                                        verbose_name="Visa Sponsorship", choices=VISA_SPONSORSHIP)

    JOB_TYPE = get_job_type()
    job_type = models.CharField(default="Full-time", max_length=50, choices=JOB_TYPE,
                                verbose_name="Job Type")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Job Applications"


class ApplicationProgressStatus(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='progress_statuses')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress_statuses')
    INTEREST_LEVELS = get_interest_level()
    interest_level = models.CharField(default="Medium", max_length=20, choices=INTEREST_LEVELS,
                                      verbose_name="Interest Level")

    APPLICATION_STATUSES = get_application_status()
    application_status = models.CharField(default="Pending", max_length=50, choices=APPLICATION_STATUSES,
                                          verbose_name="Application Status")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.application} - {self.get_application_status_display()}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Progress Statuses"


class Contact(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='contacts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number", blank=True, null=True)
    notes = models.TextField(verbose_name="Notes", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contacts"


class Communication(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='communications')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='communications')
    communication_subject = models.CharField(max_length=255, verbose_name="Communication Subject", blank=True,
                                             null=True)
    communication_summary = models.TextField(verbose_name="Communication Summary", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Communication for {self.application.job_title} at {self.application.company_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Communications"


class FollowUpMessage(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='follow_up_messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follow_up_messages')
    receivers_email = models.EmailField(verbose_name="Receivers Email", blank=True, null=True)
    follow_up_message_subject = models.CharField(max_length=255, verbose_name="Follow-up Message Subject", blank=True,
                                                 null=True)
    follow_up_message = models.TextField(max_length=3500, verbose_name="Follow-up Message", blank=True, null=True)
    scheduled_send_date = models.DateTimeField(verbose_name="Scheduled Send Date", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Follow-up message for {self.application.job_title} at {self.application.company_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Follow-up Messages"


class CoverLetter(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='cover_letters')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cover_letters')
    subject = models.CharField(max_length=255, verbose_name="Subject", blank=True, null=True)
    assistant_observation = models.TextField(max_length=3500, verbose_name="Assistant Observation", blank=True,
                                             null=True)
    letter = models.TextField(max_length=3500, verbose_name="Cover Letter", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.application.company_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Cover Letters"


class Resume(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='resumes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    resume_name = models.CharField(max_length=255, verbose_name="Full Name", blank=True, null=True)
    resume_email = models.EmailField(verbose_name="Email Address", blank=True, null=True)
    assistant_observation = models.TextField(verbose_name="Assistant Observation", blank=True, null=True)
    assistant_resume = models.TextField(verbose_name="Assistant Resume", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resume_name} - {self.application.company_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Resumes"


def upload_to(instance, filename):
    if instance.document_type == 'resume':
        return os.path.join('user_application_documents', 'Resume', filename)
    elif instance.document_type == 'cover_letter':
        return os.path.join('user_application_documents', 'Cover_letter', filename)
    return os.path.join('user_application_documents', 'Other', filename)


class Document(models.Model):
    DOCUMENT_TYPES = (
        ('resume', 'Resume'),
        ('cover_letter', 'Cover Letter'),
    )

    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='documents')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES, verbose_name="Document Type")
    file = models.FileField(upload_to=upload_to, verbose_name="Document File")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_document_type_display()} for {self.application}"

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = "Documents"


class InterviewPreparation(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='interview_preparations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='interview_preparations')
    title = models.CharField(max_length=255, verbose_name="Preparation Title", blank=True, null=True)
    about_company = models.CharField(max_length=255, verbose_name="About Company", blank=True, null=True)
    prep_questions = models.TextField(verbose_name="Preparation Question", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Interview Preparation for {self.application.company_name} by {self.user.username}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Interview Preparations"


class ApplicationCredential(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='application_credentials')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_credentials')
    username = models.CharField(max_length=255, verbose_name="Application Username")
    password = models.CharField(max_length=255, verbose_name="Application Password")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.application}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Application Credentials"
