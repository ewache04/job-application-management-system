# ManageJobApplications/utils/cover_letter/save_cover_letter_document.py
from ManageJobApplications.models import Document


def save_cover_letter_document(application, user, cover_letter_file):
    """
    Save a cover letter document to the database.

    Parameters:
    - application (JobApplication): The job application the document is associated with.
    - user (User): The user uploading the document.
    - cover_letter_file (File): The cover letter file being uploaded.

    Returns:
    - document (Document): The saved document instance.
    """
    # Create a new Document instance with the provided parameters
    document = Document(
        application=application,
        user=user,
        document_type='cover_letter',  # Specify the document type as 'cover_letter'
        file=cover_letter_file  # Set the file field to the uploaded cover letter file
    )
    # Save the document instance to the database
    document.save()
    # Return the saved document instance
    return document
