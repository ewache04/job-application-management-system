# Generated by Django 4.2.11 on 2024-07-12 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Your Job Title')),
                ('company', models.CharField(max_length=100, verbose_name='Company Name')),
                ('job_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Freelance', 'Freelance'), ('Internship', 'Internship'), ('Temporary', 'Temporary'), ('Remote', 'Remote')], default='Full-time', max_length=50, verbose_name='Job Type')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('description', models.TextField(verbose_name='Description of Role')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobProfileProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_subject', models.CharField(blank=True, max_length=255, verbose_name='Job Title')),
                ('project_summary', models.TextField(blank=True, null=True, verbose_name='Project Summary')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='ManageJobProfile.jobprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_profile_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Job Profile Projects',
                'ordering': ['-created_at'],
            },
        ),
    ]
