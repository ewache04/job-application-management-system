import os
import tempfile


def save_file_temporarily(file):
    """
    Save the uploaded file temporarily and return the file path.

    :param file: InMemoryUploadedFile object representing the uploaded file
    :return: The path to the temporary file
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as temp_file:
        for chunk in file.chunks():
            temp_file.write(chunk)
        return temp_file.name
