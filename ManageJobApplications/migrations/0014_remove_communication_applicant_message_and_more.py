# Generated by Django 4.2.11 on 2024-06-25 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageJobApplications', '0013_remove_contact_job_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communication',
            name='applicant_message',
        ),
        migrations.RemoveField(
            model_name='communication',
            name='company_message',
        ),
    ]