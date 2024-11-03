# ManageJobApplications/views/cover_letter/add_cover_letter/add_cover_letter/generate_and_save_cover_letter.py
from ManageJobApplications.data_authentication_process.auth_cover_letter_data.get_cover_letter_form_data import get_cover_letter_form_data
from ManageJobApplications.utils.cover_leter.process_cover_letter_file import process_cover_letter_file
from ManageJobApplications.views.cover_letter.add_cover_letter.save_cover_letter import save_cover_letter
from general_utils.error_logging import log_error


def generate_and_save_cover_letter(request, client=None, user=None, application=None, career_summary=None, resume=None, raw_cover_letter=None):
    try:
        # Process the cover letter file
        raw_cover_letter, document = process_cover_letter_file(request, client, user, application, raw_cover_letter)

        if raw_cover_letter is None:
            raise ValueError("Cover letter could not be created from the provided file or text.")

        # Get valid cover letter data
        valid_cover_letter_data = get_cover_letter_form_data(client, user, application,
                                                             career_summary, resume, raw_cover_letter)

        if not valid_cover_letter_data:
            raise ValueError("Generated cover letter data is not valid.")

        # Save the cover letter
        cover_letter = save_cover_letter(application, user, valid_cover_letter_data)
        print('Cover letter saved successfully')
        return cover_letter

    except Exception as e:
        log_error(f"An error occurred while generating and saving the cover letter: {str(e)}")
        return None
