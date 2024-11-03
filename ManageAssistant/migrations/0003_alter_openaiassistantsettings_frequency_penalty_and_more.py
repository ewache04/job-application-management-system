# Generated by Django 4.2.11 on 2024-07-09 00:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageAssistant', '0002_alter_openaiassistantsettings_frequency_penalty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openaiassistantsettings',
            name='frequency_penalty',
            field=models.FloatField(default=0.2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Frequency Penalty'),
        ),
        migrations.AlterField(
            model_name='openaiassistantsettings',
            name='presence_penalty',
            field=models.FloatField(default=0.2, verbose_name='Presence Penalty'),
        ),
        migrations.AlterField(
            model_name='openaiassistantsettings',
            name='top_p',
            field=models.FloatField(default=0.1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Top P'),
        ),
    ]
