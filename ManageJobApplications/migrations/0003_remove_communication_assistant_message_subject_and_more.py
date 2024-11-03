# Generated by Django 4.2.11 on 2024-06-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageJobApplications', '0002_resume_resume_key_words_found_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communication',
            name='assistant_message_subject',
        ),
        migrations.AddField(
            model_name='communication',
            name='communication_subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Communication Subject'),
        ),
        migrations.AddField(
            model_name='communication',
            name='communication_summary',
            field=models.TextField(blank=True, null=True, verbose_name='Communication Summary'),
        ),
    ]