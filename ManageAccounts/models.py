# ManageAccounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username if self.username else "User"
