# Generated by Django 4.2.11 on 2024-06-06 13:11

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
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_posting_urls', models.URLField(blank=True, max_length=1500, null=True, verbose_name='Job Posting URLs')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, max_length=255, verbose_name='Job Title')),
                ('job_id', models.CharField(blank=True, max_length=255, verbose_name='Job id')),
                ('location', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('job_posting_summary', models.TextField(blank=True, max_length=3500, null=True, verbose_name='Application Description')),
                ('application_deadline', models.DateField(blank=True, null=True, verbose_name='Application Deadline')),
                ('visa_sponsorship', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=25, verbose_name='Visa Sponsorship')),
                ('good_luck_message', models.CharField(blank=True, default='All the best', max_length=100, null=True, verbose_name='Good Luck Message')),
                ('job_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Freelance', 'Freelance'), ('Internship', 'Internship'), ('Temporary', 'Temporary'), ('Remote', 'Remote')], default='Full-time', max_length=50, verbose_name='Job Type')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Job Applications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Full Name')),
                ('resume_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('resume_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('resume_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Home Address')),
                ('resume_summary', models.TextField(blank=True, null=True, verbose_name='Summary')),
                ('resume_education', models.TextField(blank=True, null=True, verbose_name='Education')),
                ('resume_experience', models.TextField(blank=True, null=True, verbose_name='Work Experience')),
                ('resume_projects', models.TextField(blank=True, null=True, verbose_name='Projects')),
                ('resume_skills', models.TextField(blank=True, null=True, verbose_name='Skills')),
                ('resume_certifications', models.TextField(blank=True, null=True, verbose_name='Certifications')),
                ('resume_languages', models.TextField(blank=True, null=True, verbose_name='Languages')),
                ('resume_hobbies', models.TextField(blank=True, null=True, verbose_name='Hobbies and Interests')),
                ('resume_references', models.TextField(blank=True, null=True, verbose_name='References')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Resumes',
                'ordering': ['-created_at'],
            },
        ),
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
            name='FollowUpMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivers_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Receivers Email')),
                ('follow_up_message_subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='Follow-up Message Subject')),
                ('follow_up_message', models.TextField(blank=True, null=True, verbose_name='Follow-up Message')),
                ('scheduled_send_date', models.DateTimeField(blank=True, null=True, verbose_name='Scheduled Send Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_up_messages', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_up_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Follow-up Messages',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subject')),
                ('letter', models.TextField(blank=True, null=True, verbose_name='Cover Letter')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cover_letters', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cover_letters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cover Letters',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('job_title', models.CharField(blank=True, max_length=20, null=True, verbose_name='Job Title')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistant_message_subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='Assistant Message Subject')),
                ('company_message', models.TextField(blank=True, null=True, verbose_name='Company Message')),
                ('applicant_message', models.TextField(blank=True, null=True, verbose_name='Applicant Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communications', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Communications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationProgressStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_level', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium', max_length=20, verbose_name='Interest Level')),
                ('application_status', models.CharField(choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Interview Scheduled', 'Interview Scheduled'), ('Interview Completed', 'Interview Completed'), ('Offer Extended', 'Offer Extended'), ('Offer Accepted', 'Offer Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=50, verbose_name='Application Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_statuses', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_statuses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Progress Statuses',
                'ordering': ['-created_at'],
            },
        ),
    ]
