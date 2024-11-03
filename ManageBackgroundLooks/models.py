from django.db import models
from django.conf import settings  # Import settings module to access AUTH_USER_MODEL

from . import background_choices


class MyBackgroundLooks(models.Model):
    background_choices = background_choices.background_choices()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selected_background = models.CharField(default="white",  max_length=100, choices=background_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Background Image {self.id}" if self.id else "Selected Image"

