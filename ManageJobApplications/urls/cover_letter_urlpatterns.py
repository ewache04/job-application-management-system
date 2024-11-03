# ManageJobApplications/urls/cover_letter_urlpatterns.py
from django.urls import path



def get_cover_letter_urlpatterns():
    """
    Retrieve URL patterns for cover letter-related views.

    This function defines URL patterns for cover letter-related views, including adding, updating,
    deleting, and listing cover letters.

    Returns:
        list: A list of URL patterns for cover letter-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.cover_letter.add_cover_letter import add_cover_letter
    from ManageJobApplications.views.cover_letter.cover_letter_details import cover_letter_details
    from ManageJobApplications.views.cover_letter.delete_confirmation_cover_letter import delete_confirmation_cover_letter
    from ManageJobApplications.views.cover_letter.update_cover_letter import update_cover_letter

    # Define URL patterns for cover letters
    return [
        # Cover letter management URLs
        path('application/<int:application_id>/add_cover_letter/', add_cover_letter.add_cover_letter, name='add_cover_letter'),
        path('application/<int:application_id>/update_cover_letter/<int:cover_letter_id>/', update_cover_letter.update_cover_letter, name='update_cover_letter'),
        path('application/<int:application_id>/delete_confirmation_cover_letter/<int:cover_letter_id>/', delete_confirmation_cover_letter.delete_confirmation_cover_letter, name='delete_confirmation_cover_letter'),
        path('application/<int:application_id>/cover_letter_details/<int:cover_letter_id>/',
             cover_letter_details.cover_letter_details, name='cover_letter_details'),
    ]
