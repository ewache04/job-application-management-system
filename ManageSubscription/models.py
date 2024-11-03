# ManageSubscription/models.py
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from ManageAccounts.models import CustomUser
from OpenColabAI import settings


class UserPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    subscription_active = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)

    @receiver(post_save, sender=CustomUser)
    def create_user_payment(sender, instance, created, **kwargs):
        if created:
            UserPayment.objects.create(user=instance)
