# ManageJobApplications/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone


from ManageJobApplications.utils.get_job_type import get_job_type


class JobProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Your Job Title")
    company = models.CharField(max_length=100, verbose_name="Company Name")
    JOB_TYPE = get_job_type()
    job_type = models.CharField(default="Full-time", max_length=50, choices=JOB_TYPE, verbose_name="Job Type")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    description = models.TextField(verbose_name="Description of Role")
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Type: Job Profile\n"
                f"Names: {self.user.first_name} {self.user.last_name}\n"
                f"Title: {self.title}\n"
                f"Company Name: {self.company}\n"
                f"Duration: {self.start_date} to {self.end_date}\n"
                f"Description: {self.description}")


class JobProfileProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_profile_projects')
    job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE, related_name='projects')
    project_subject = models.CharField(max_length=255, verbose_name="Job Title", blank=True)
    project_summary = models.TextField(verbose_name="Project Summary", blank=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_profile}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Job Profile Projects"

