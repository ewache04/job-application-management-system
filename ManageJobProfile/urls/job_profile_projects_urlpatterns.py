# ManageJobApplications/urls/job_profile_projects_urlpatterns.py
from django.urls import path


def get_job_profile_projects_urlpatterns():
    """
    Retrieve URL patterns for job profile-related views.

    This function defines URL patterns for job profile-related views, including listing, adding,
    updating, and deleting job profiles.

    Returns:
        list: A list of URL patterns for job profile-related views.
    """
    # Import necessary modules

    from ManageJobProfile.views.job_profile_projects.add_job_profile_project import add_job_profile_project
    from ManageJobProfile.views.job_profile_projects.confirm_delete_job_profile_project import \
        confirm_delete_job_profile_project
    from ManageJobProfile.views.job_profile_projects.job_profile_project_details import job_profile_project_details
    from ManageJobProfile.views.job_profile_projects.job_profile_projects_list import job_profile_projects_list
    from ManageJobProfile.views.job_profile_projects.update_job_profile_project import update_job_profile_project

    # Define URL patterns
    job_profile_projects_urlpatterns = [
        # Job profile management URLs
        path('user/<int:user_id>/job_profile_details/<int:job_profile_id>/job_profile_projects_list/',
             job_profile_projects_list.job_profile_projects_list, name='job_profile_projects_list'),

        path('user/<int:user_id>/job_profile_details/<int:job_profile_id>/job_profile_project_details/<int'
             ':job_profile_project_id>/',
             job_profile_project_details.job_profile_project_details,
             name='job_profile_project_details'),

        path(
            'user/<int:user_id>/job_profile_details/<int:job_profile_id>/add_job_profile_project/',
            add_job_profile_project.add_job_profile_project,
            name='add_job_profile_project'),

        path(
            'user/<int:user_id>/job_profile_details/<int:job_profile_id>/update_job_profile_project/<int'
            ':job_profile_project_id>/',
            update_job_profile_project.update_job_profile_project,
            name='update_job_profile_project'),

        path(
            'user/<int:user_id>/job_profile_details/<int:job_profile_id>/confirm_delete_job_profile_project/<int'
            ':job_profile_project_id>/',
            confirm_delete_job_profile_project.confirm_delete_job_profile_project,
            name='confirm_delete_job_profile_project'),

    ]

    return job_profile_projects_urlpatterns
