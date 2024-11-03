# ManageAssistant/open_model_group.py
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from openai_tools.openai_models import get_openai_models


class OpenAIAssistantSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assistant_settings')

    # Get model choices
    MODEL_CHOICES = get_openai_models()

    selected_model = models.CharField(max_length=100, choices=MODEL_CHOICES,
                                      verbose_name="Selected Model")

    # Default model set to "gpt-3.5-turbo"
    max_tokens = models.PositiveIntegerField(default=4096,
                                             verbose_name="Max Tokens",
                                             validators=[MinValueValidator(0), MaxValueValidator(4096)])

    temperature = models.FloatField(default=0.2, verbose_name="Temperature",
                                    validators=[MinValueValidator(0), MaxValueValidator(2)])

    top_p = models.FloatField(default=0.1, verbose_name="Top P",
                              validators=[MinValueValidator(0), MaxValueValidator(1)])

    frequency_penalty = models.FloatField(default=0.2,
                                          verbose_name="Frequency Penalty",
                                          validators=[MinValueValidator(0), MaxValueValidator(1)])

    presence_penalty = models.FloatField(default=0.2,
                                         verbose_name="Presence Penalty")

    def __str__(self):
        return f"Assistant Settings for {self.user.username}"
