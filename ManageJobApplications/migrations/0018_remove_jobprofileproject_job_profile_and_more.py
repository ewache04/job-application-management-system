# Generated by Django 4.2.11 on 2024-07-16 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageJobApplications', '0017_jobprofileproject_project_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobprofileproject',
            name='job_profile',
        ),
        migrations.RemoveField(
            model_name='jobprofileproject',
            name='user',
        ),
        migrations.DeleteModel(
            name='JobProfile',
        ),
        migrations.DeleteModel(
            name='JobProfileProject',
        ),
    ]
