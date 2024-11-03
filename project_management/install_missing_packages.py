# project_management/install_missing_packages.py
import subprocess
import sys

from project_management.run_dev_server import runserver


def install_missing_packages():
    try:
        # Path to the requirements.txt file
        requirements_file = "requirements.txt"

        with open(requirements_file, 'r') as f:
            required_packages = f.read().splitlines()

        installed_packages = [package.split('==')[0] for package in
                              subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode().split('\n')[2:] if
                              package]
        missing_packages = [package for package in required_packages if
                            package.split('==')[0] not in installed_packages]

        if missing_packages:
            print("Installing missing packages:")
            for package in missing_packages:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print("All missing packages have been installed successfully!")
        else:
            print("All required packages are already installed.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Install missing packages first
    install_missing_packages()
    runserver()
