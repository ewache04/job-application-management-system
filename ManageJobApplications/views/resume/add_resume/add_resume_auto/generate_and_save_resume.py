# ManageJobApplications/views/resume/add_resume/add_resume_auto/generate_and_save_resume.py
from ManageJobApplications.data_authentication_process.auth_resume_data.get_valid_resume_data import \
    get_resume_form_data
from ManageJobApplications.utils.resume.process_resume_file import process_resume_file
from ManageJobApplications.views.resume.add_resume.add_resume_auto.save_resume import save_resume
from general_utils.error_logging import log_error


def generate_and_save_resume(request, client, user, application, career_summary, raw_resume):

    """
    Generate and save a resume using provided details and the assistant client.

    Parameters:
    - client: The client object for interacting with the assistant.
    - user: The user for whom the resume is being generated.
    - application: The job application the resume is for.
    - work_experience: Optional work experience details.
    - raw_resume: Optional raw resume text.

    Returns:
    - The saved resume object if successful, None otherwise.
    """
    try:
        # Process the resume file or raw resume text
        print("Start generating and saving resume...")  # Debugging output
        resume, resume_file = process_resume_file(request, client, user,
                                                  application, career_summary, raw_resume)

        print(f"Processed resume: {resume}")
        print(f"Processed resume file: {resume_file}")

        if resume is None:
            print("Resume could not be created from the provided file or text.")
            raise ValueError("Resume could not be created from the provided file or text.")

        # Get valid resume data
        valid_resume_data = get_resume_form_data(client, user, application,
                                                 career_summary, resume)

        print(f"Valid resume data: {valid_resume_data}")

        if not valid_resume_data:
            raise ValueError("Generated resume data is not valid.")

        # Save the resume
        saved_resume = save_resume(application, user, valid_resume_data)
        print('Resume saved successfully')
        return saved_resume

    except Exception as e:
        log_error(f"An error occurred while generating and saving the resume: {str(e)}")
        return None
