import os
import subprocess


def ensure_pandoc_installed():
    try:
        import pypandoc
        try:
            # Attempt to get Pandoc version
            pypandoc.get_pandoc_version()
        except OSError:
            pypandoc.download_pandoc()
    except ImportError:
        # Install pypandoc if it's not installed
        subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', 'pypandoc'])
        import pypandoc
        pypandoc.download_pandoc()