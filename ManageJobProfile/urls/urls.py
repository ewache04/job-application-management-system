# ManageJobProfile/urls/urls.py


def initialize_urlpatterns():
    """
    Function to initialize URL patterns for the ManageJobApplications app.

    Returns:
    List: A list containing all the URL patterns.
    """
    # Import URL pattern functions from submodules
    from ManageJobProfile.urls.job_profile_projects_urlpatterns import get_job_profile_projects_urlpatterns
    from ManageJobProfile.urls.job_profile_urlpatterns import get_job_profile_urlpatterns

    print("Initializing ManageJobApplication URL patterns")

    # Initialize an empty list to store URL patterns
    urlpatterns = []

    # Add job profile URL patterns
    urlpatterns += get_job_profile_urlpatterns()

    # Add job profile projects URL patterns
    urlpatterns += get_job_profile_projects_urlpatterns()

    # Print a message indicating completion of URL pattern initialization
    print("Completed initializing URL patterns")

    # Return the list of URL patterns
    return urlpatterns
