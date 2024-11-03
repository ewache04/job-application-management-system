# ManageJobApplications/urls/contact_urlpatterns.py
from django.urls import path


def get_contact_urlpatterns():
    """
    Retrieve URL patterns for contact-related views.

    This function defines URL patterns for contact-related views, including adding, updating, deleting,
    and viewing contact details.

    Returns:
        list: A list of URL patterns for contact-related views.
    """
    # Import necessary modules
    from ManageJobApplications.views.contacts.add_contact import add_contact
    from ManageJobApplications.views.contacts.contact_details import contact_details
    from ManageJobApplications.views.contacts.contact_list import contact_list
    from ManageJobApplications.views.contacts.delete_confirmation_contact import delete_confirmation_contact
    from ManageJobApplications.views.contacts.update_contact import update_contact

    # Define URL patterns for contact-related views
    return [
        # Contact management URLs

        path('application/<int:application_id>/contact_list/',
             contact_list.contact_list, name='contact_list'),

        path('application/<int:application_id>/contacts/contact_details/<int:contact_id>/',
             contact_details.contact_details, name='contact_details'),

        path('application/<int:application_id>/contact/update_contact/<int:contact_id>/',
             update_contact.update_contact, name='update_contact'),

        path('application/<int:application_id>/contact/delete_confirmation_contact/<int:contact_id>/',
             delete_confirmation_contact.delete_confirmation_contact,
             name='delete_confirmation_contact'),

        path('application/<int:application_id>/add_contact/', add_contact.add_contact, name='add_contact'),



        path('application/delete_confirmation_contact/<int:pk>/',
             delete_confirmation_contact.delete_confirmation_contact,
             name='delete_confirmation_contact'),

    ]
