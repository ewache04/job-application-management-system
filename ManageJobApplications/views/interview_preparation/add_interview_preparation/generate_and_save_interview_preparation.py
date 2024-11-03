# ManageJobApplications/views/interview_preparation/add_interview_preparation/add_interview_preparation/generate_and_save_interview_preparation.py
from ManageJobApplications.data_authentication_process.auth_interview_preparation_data.get_valid_interview_prep_data import \
    get_interview_prep_form_data
from ManageJobApplications.views.interview_preparation.add_interview_preparation.save_interview_preparation import \
    save_interview_preparation
from general_utils.error_logging import log_error


def generate_and_save_interview_preparation(request, client, user,
                                            application, career_summary=None,
                                            raw_interview_preparation=None):
    """
    Generate and save interview preparation details for a job application.

    Parameters:
    - client: The client object for communicating with the assistant.
    - user: The user object containing user details.
    - application: The application object containing job application details.
    - work_experience: The work experience details of the user.

    Returns:
    - InterviewPreparation object if successful, None otherwise.
    """
    try:
        valid_interview_preparation_data = get_interview_prep_form_data(client, user, application, career_summary)

        interview_preparation = save_interview_preparation(application, user, valid_interview_preparation_data)
        if interview_preparation:
            return interview_preparation
        else:
            return None

    except Exception as e:
        log_error(f"An error occurred while generating and saving interview preparation: {str(e)}")
        print(f"An error occurred while generating and saving interview preparation: {str(e)}")
        return None
