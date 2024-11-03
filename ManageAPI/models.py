from django.db import models
from django.conf import settings  # Import settings module to access AUTH_USER_MODEL

from . import key_names


class UserKey(models.Model):
    key_names = key_names.key_names()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key_name = models.CharField(max_length=100, choices=key_names)
    key_value = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"key_name {self.id}" if self.id else "key_name"

    def save(self, *args, **kwargs):
        # Check if the user has more than 5 keys associated with the current key_name
        if UserKey.objects.filter(user=self.user, key_name=self.key_name).count() >= 5:
            # Raise an exception or handle the error accordingly
            raise ValueError("User cannot have more than 5 keys associated with each key_name.")

        # Check if the key being saved is set as default
        if self.is_default:
            # Set is_default to False for all other keys with the same user and key_name
            UserKey.objects.filter(user=self.user, key_name=self.key_name).exclude(pk=self.pk).update(is_default=False)

        super().save(*args, **kwargs)
