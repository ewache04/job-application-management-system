# project_management/__init__.py

import os

# Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenColabAI.settings')

# Django setup
import django

django.setup()

# Import necessary modules after Django setup
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# Import the necessary modules
from django.core.management import call_command
from django.apps import apps
