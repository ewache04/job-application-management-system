# ManageJobApplications/views/documents/get_last_document.py
from ManageJobApplications.models import Document


def get_last_document(application, document_type):
    document = Document.objects.filter(application=application, document_type=document_type).last()
    return document if document else None
