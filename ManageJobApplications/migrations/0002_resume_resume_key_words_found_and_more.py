# Generated by Django 4.2.11 on 2024-06-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageJobApplications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='resume_key_words_found',
            field=models.TextField(blank=True, null=True, verbose_name='keywords Found'),
        ),
        migrations.AddField(
            model_name='resume',
            name='resume_key_words_missing',
            field=models.TextField(blank=True, null=True, verbose_name='keywords Missing'),
        ),
        migrations.AlterField(
            model_name='coverletter',
            name='letter',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='Cover Letter'),
        ),
        migrations.AlterField(
            model_name='followupmessage',
            name='follow_up_message',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='Follow-up Message'),
        ),
    ]