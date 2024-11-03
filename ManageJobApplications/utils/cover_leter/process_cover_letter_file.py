import os

from ManageJobApplications.data_authentication_process.auth_cover_letter_data.get_cover_letter_form_data import get_cover_letter_form_data
from ManageJobApplications.utils.cover_leter.save_cover_letter_document import save_cover_letter_document
from ManageJobApplications.utils.file_converter.convert_file_to_text import convert_file_to_text
from ManageJobApplications.utils.file_converter.ensure_pandoc_installed import ensure_pandoc_installed
from ManageJobApplications.utils.file_converter.temporary_file_handler import save_file_temporarily
from ManageJobApplications.views.cover_letter.add_cover_letter.save_cover_letter import save_cover_letter


def process_cover_letter_file(request, client, user,
                              application=None, raw_cover_letter=None):
    if 'cover_letter_file' in request.FILES:
        cover_letter_file = request.FILES['cover_letter_file']

        # Save the file temporarily
        temp_file_path = save_file_temporarily(cover_letter_file)

        try:
            # Ensure Pandoc is available
            ensure_pandoc_installed()

            # Convert the file to text
            raw_cover_letter = str(raw_cover_letter) + str(convert_file_to_text(temp_file_path))

            # Generate cover letter data
            valid_cover_letter_data = get_cover_letter_form_data(client, user, raw_cover_letter)

            if not valid_cover_letter_data:
                raise ValueError("Generated cover letter data is not valid.")

            # Save cover letter using the extracted data
            cover_letter = save_cover_letter(application, user, valid_cover_letter_data)
            save_cover_letter_document(application, user, cover_letter_file)
            print('Your cover letter has been created successfully.')
            return cover_letter, cover_letter_file
        finally:
            # Ensure the temporary file is deleted
            os.remove(temp_file_path)
    else:
        # If no file is provided, process the raw cover letter text
        if raw_cover_letter:
            return raw_cover_letter, None
        else:
            return None, None
