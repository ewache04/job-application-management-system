# project_management/activate_venv.py
import os


def activate_venv():
    # Activate the virtual environment
    venv_activate_path = os.path.join(os.getcwd(), ".venv", "scripts", "activate.bat")
    if os.path.exists(venv_activate_path):
        print("Activating virtual environment...")
        exec(open(venv_activate_path).read(), {'__file__': venv_activate_path})
        print("Virtual environment was successfully activated...")
    else:
        print("Failed to activate virtual environment. Please check your setup.")


if __name__ == "__main__":
    activate_venv()
