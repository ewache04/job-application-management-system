# Generated by Django 4.2.11 on 2024-06-18 19:34

import ManageJobApplications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageJobApplications', '0006_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='resume_address',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_certifications',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_education',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_experience',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_hobbies',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_key_words_found',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_key_words_missing',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_languages',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_phone',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_projects',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_references',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='resume_skills',
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=ManageJobApplications.models.upload_to, verbose_name='Document File'),
        ),
    ]
