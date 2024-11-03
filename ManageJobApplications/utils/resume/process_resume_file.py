import os
from ManageJobApplications.data_authentication_process.auth_resume_data.get_valid_resume_data import \
    get_resume_form_data
from ManageJobApplications.utils.resume.save_resume_document import save_resume_document
from ManageJobApplications.utils.file_converter.convert_file_to_text import convert_file_to_text
from ManageJobApplications.utils.file_converter.ensure_pandoc_installed import ensure_pandoc_installed
from ManageJobApplications.utils.file_converter.temporary_file_handler import save_file_temporarily
from ManageJobApplications.views.resume.add_resume.add_resume_auto.save_resume import save_resume


def process_resume_file(request, client, user, application=None, work_experience=None, raw_resume=None):
    """
    Process the uploaded or raw resume file.

    Parameters:
    - request: The HTTP request object containing the resume file.
    - client: The client object for interacting with the assistant.
    - user: The user uploading the resume.
    - application: The job application the resume is for.
    - work_experience: Optional work experience details.
    - raw_resume: Optional raw resume text.

    Returns:
    - tuple: The resume object and the resume file, if successful; otherwise, None, None.
    """
    print("Starting process_resume_file...")  # Debugging output

    # Check if the resume file is in the request
    if 'resume_file' in request.FILES:
        resume_file = request.FILES['resume_file']
        print(f"Received resume file: {resume_file.name}")  # Debugging output

        # Save the file temporarily
        temp_file_path = save_file_temporarily(resume_file)
        print(f"Temporary file path: {temp_file_path}")  # Debugging output

        try:
            # Ensure Pandoc is available
            ensure_pandoc_installed()
            print("Pandoc is installed.")  # Debugging output

            # Convert the file to text
            raw_resume_text = convert_file_to_text(temp_file_path)
            print(f"Converted resume text: {raw_resume_text[:100]}...")  # Print first 100 characters for debugging

            # Combine with any existing raw resume text
            raw_resume = (raw_resume or "") + raw_resume_text
            print(f"Final raw resume text: {raw_resume[:100]}...")  # Print first 100 characters for debugging

            # Generate resume data
            valid_resume_data = get_resume_form_data(client, user, application, work_experience, raw_resume)
            print(f"Valid resume data: {valid_resume_data}")  # Debugging output

            if not valid_resume_data:
                raise ValueError("Generated resume data is not valid.")

            # Save resume using the extracted data
            resume = save_resume(application, user, valid_resume_data)
            save_resume_document(application, user, resume_file)
            print('Your resume has been created successfully.')
            return resume, resume_file

        except Exception as e:
            print(f"Error occurred: {e}")  # Debugging output
        finally:
            # Ensure the temporary file is deleted
            os.remove(temp_file_path)
            print(f"Temporary file {temp_file_path} deleted.")  # Debugging output
    else:
        print("No resume file found in the request.")  # Debugging output

        # If no file is provided, process the raw resume text
        if raw_resume:
            print("Processing raw resume text.")  # Debugging output
            return raw_resume, None
        else:
            print("No raw resume text provided.")  # Debugging output
            return None, None
