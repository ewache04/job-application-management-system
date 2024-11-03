# ManageCareerSummary/models.py
from django.db import models

from OpenColabAI import settings


# Create your models here.
class MyCareerSummary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='career_summary')

    career_summary = models.TextField(verbose_name="Career Summary", blank=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"USer {self.user}"
                f" career summary {self.career_summary}"
                )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Career Summary"
