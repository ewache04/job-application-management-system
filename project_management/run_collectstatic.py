# project_management/run_collectstatic.py

# Import necessary modules
import os
from django.core.management import call_command

from project_management.run_dev_server import runserver

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenColabAI.settings')
import django

django.setup()


# Define a function to run collectstatic
def run_collectstatic():
    print("Running collectstatic...")
    call_command('collectstatic', interactive=False, verbosity=0)
    print("Collectstatic completed successfully!")


# Call the function to run collectstatic
if __name__ == "__main__":
    run_collectstatic()
    runserver()
