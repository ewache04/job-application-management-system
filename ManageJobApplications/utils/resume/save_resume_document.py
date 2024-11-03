# ManageJobApplications/utils/resume/save_resume_document.py
from ManageJobApplications.models import Document


def save_resume_document(application, user, resume_file):
    """
    Save a resume document to the database.

    Parameters:
    - application: The job application the document is associated with.
    - user: The user uploading the document.
    - resume_file: The resume file being uploaded.

    Returns:
    - document: The saved document instance.
    """
    # Create a new Document instance with the provided parameters
    document = Document(
        application=application,
        user=user,
        document_type='resume',  # Specify the document type as 'resume'
        file=resume_file  # Set the file field to the uploaded resume file
    )
    # Save the document instance to the database
    document.save()
    # Return the saved document instance
    return document
