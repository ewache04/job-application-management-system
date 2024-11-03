# Generated by Django 4.2.11 on 2024-06-10 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageJobApplications', '0003_remove_communication_assistant_message_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Application Username')),
                ('password', models.CharField(max_length=255, verbose_name='Application Password')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_credentials', to='ManageJobApplications.jobapplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_credentials', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Application Credentials',
                'ordering': ['-created_at'],
            },
        ),
    ]
