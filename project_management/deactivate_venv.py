# project_management/run_dev_server.py
from project_management.activate_venv import activate_venv
import subprocess


def runserver():
    # Run the development server
    print("Starting development server...")
    subprocess.run(["python", "manage.py", "runserver"], shell=True)
    print("Development server started!...")


if __name__ == "__main__":
    activate_venv()
    runserver()
