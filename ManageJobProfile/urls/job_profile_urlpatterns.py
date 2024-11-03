# ManageJobApplications/urls/job_profile_urlpatterns.py
from django.urls import path


def get_job_profile_urlpatterns():
    """
    Retrieve URL patterns for job profile-related views.

    This function defines URL patterns for job profile-related views, including listing, adding,
    updating, and deleting job profiles.

    Returns:
        list: A list of URL patterns for job profile-related views.
    """
    # Import necessary modules
    from ManageJobProfile.views.jobs.add_job_profile import add_job_profile
    from ManageJobProfile.views.jobs.confirm_delete_job_profile import confirm_delete_job_profile
    from ManageJobProfile.views.jobs.job_profile_details import job_profile_details
    from ManageJobProfile.views.jobs.job_profile_list import job_profile_list
    from ManageJobProfile.views.jobs.update_job_profile import update_job_profile

    # Define URL patterns
    job_profile_urlpatterns = [
        # Job profile management URLs
        path('user/<int:user_id>/job_profile_list/',
             job_profile_list.job_profile_list, name='job_profile_list'),

        path('user/<int:user_id>/job_profile_details/<int:job_profile_id>/',
             job_profile_details.job_profile_details,
             name='job_profile_details'),

        path('user/<int:user_id>/add_job_profile/',
             add_job_profile.add_job_profile, name='add_job_profile'),

        path('user/<int:user_id>/update_job_profile/<int:job_profile_id>/',
             update_job_profile.update_job_profile,
             name='update_job_profile'),

        path('user/<int:user_id>/confirm_delete_job_profile/<int:job_profile_id>/',
             confirm_delete_job_profile.confirm_delete_job_profile,
             name='confirm_delete_job_profile'),
    ]

    return job_profile_urlpatterns
