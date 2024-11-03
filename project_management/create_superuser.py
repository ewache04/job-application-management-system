# project_management/create_superuser.py

# Import necessary modules
import os
import django

from project_management.run_dev_server import runserver
# Import the custom user model
from django.contrib.auth import get_user_model

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenColabAI.settings')
django.setup()


# Define a function to create a superuser
def create_superuser(username, email, password):
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")


# Call the function to create a superuser
if __name__ == "__main__":
    create_superuser('superuser1', 'superuser1@gmail.com', '@superuser1_admin')
    runserver()
