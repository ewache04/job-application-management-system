# ManageJobApplications/communication/communication_extraction_format.py

def job_profile_project_extraction_structure():
    """
    Return the expected structure for extracting job profile project details.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected structure.
    """
    structure = [
        ('project_subject', "Enter a short and concise title for the project here."),
        ('project_summary',
            "Enter a well-detailed project summary in a bullet point format. Ensure you capture all "
            "valuable information and present it clearly.")
    ]

    return structure
