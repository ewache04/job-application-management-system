# project_management/run_dev_server.py

from project_management import call_command


def runserver():
    # Run the development server
    print("Starting development server...")
    call_command('runserver', verbosity=0)
    print("Development server started!...")


# Usage
if __name__ == "__main__":
    runserver()
