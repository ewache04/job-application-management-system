# ManageJobApplications/urls.py


def initialize_urlpatterns():
    """
    Function to initialize URL patterns for the ManageJobApplications app.

    Returns:
    List: A list containing all the URL patterns.
    """
    # Import URL pattern functions from submodules
    from ManageJobApplications.urls.interview_preparation_urlpatterns import get_interview_preparation_urlpatterns
    from ManageJobApplications.urls.application_credentials_urlpatterns import get_application_credentials_urlpatterns
    from ManageJobApplications.urls.application_urlpatterns import get_application_urlpatterns
    from ManageJobApplications.urls.communications_urlpatterns import get_communications_urlpatterns
    from ManageJobApplications.urls.contact_urlpatterns import get_contact_urlpatterns
    from ManageJobApplications.urls.cover_letter_urlpatterns import get_cover_letter_urlpatterns
    from ManageJobApplications.urls.follow_up_messages_urlpatterns import get_follow_up_messages_urlpatterns
    from ManageJobApplications.urls.progress_status_urlpatterns import get_progress_status_urlpatterns
    from ManageJobApplications.urls.resume_urlpatterns import get_resume_urlpatterns

    print("Initializing ManageJobApplication URL patterns")

    # Initialize an empty list to store URL patterns
    urlpatterns = []

    # Add application URL patterns
    urlpatterns += get_application_urlpatterns()

    # Add communications URL patterns
    urlpatterns += get_communications_urlpatterns()

    # Add Interview preparation URL patterns
    urlpatterns += get_interview_preparation_urlpatterns()

    # Add contact URL patterns
    urlpatterns += get_contact_urlpatterns()

    # Add cover letter URL patterns
    urlpatterns += get_cover_letter_urlpatterns()

    # Add follow-up messages URL patterns
    urlpatterns += get_follow_up_messages_urlpatterns()

    # Add progress status URL patterns
    urlpatterns += get_progress_status_urlpatterns()

    # Add resume URL patterns
    urlpatterns += get_resume_urlpatterns()

    # Add application credentials URL patterns
    urlpatterns += get_application_credentials_urlpatterns()

    # Print a message indicating completion of URL pattern initialization
    print("Completed initializing URL patterns")

    # Return the list of URL patterns
    return urlpatterns
