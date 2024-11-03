# ManageJobApplications/communication/communication_extraction_format.py

def communication_extraction_structure():
    """
    Return the expected structure for extracting communication details.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected structure.
    """
    structure = [
        ('communication_subject', "Enter a short and concise subject for the communication here."),
        ('communication_summary', (
            "Enter a well-detailed summary of both the company's and the applicant's messages. Ensure you capture all "
            "valuable information and present it in a coherent article format. The objective is to highlight the "
            "message from the company and the response from the applicant. Then, provide an analysis of the "
            "interaction."
        ))
    ]

    return structure

