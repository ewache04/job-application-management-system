# Generated by Django 4.2.11 on 2024-07-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageSubscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpayment',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpayment',
            name='subscription_canceled',
            field=models.BooleanField(default=False),
        ),
    ]
