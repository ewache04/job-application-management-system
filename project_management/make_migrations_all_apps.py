# make_migrations_all_apps.py
import os
import django
from django.core.management import call_command, CommandError

from OpenColabAI import settings
from project_management.run_dev_server import runserver

# Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenColabAI.settings')

# Django setup
django.setup()

# List of app names
app_names = [app.split('.')[0] for app in settings.INSTALLED_APPS if not app.startswith('django.')]


# Define function to make migrations
def make_migrations():
    # Iterate over app names and make migrations
    for app_name in app_names:
        try:
            print(f"Making migrations for {app_name}...")
            call_command('makemigrations', app_name, verbosity=0)

        except CommandError as e:
            if "No installed app with label" not in str(e):
                print(f"Failed to make migrations for {app_name}: {e}")


# Define function to migrate
def migrate():
    # Migrate all apps
    print("Applying migrations...")
    call_command('migrate', verbosity=0)
    print("Migrations completed successfully!...")


# Main function
def main():
    make_migrations()
    migrate()
    runserver()


if __name__ == "__main__":
    main()
