# Generated by Django 4.2.11 on 2024-06-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageAccounts', '0002_remove_customuser_stripe_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]