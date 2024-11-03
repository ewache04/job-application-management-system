# ManageJobApplications/job_description_extraction_output_structure_format.py

def job_extraction_structure():
    """
    Return the expected structure for extracting job details.

    This structure outlines the necessary fields for a job description extraction
    and provides specific instructions on what to include if the information is not available.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected structure.
    """
    dataset = [
        ('job_posting_urls',
         "Enter the URL link for the job posting here (if not specified, enter 'None')"),
        ('company_name',
         "Must find and enter the name of the company here (if not specified, enter 'None')"),
        ('job_title',
         "Enter the job title here (if not specified, enter 'None')"),
        ('job_id',
         "Enter the job ID here (if not specified, enter 'None')"),
        ('location',
         "Enter the location here (if not specified, enter 'Not specified')"),
        ('application_deadline',
         "Enter in Date format as %Y-%m-%d (if not specified, enter 'None')"),
        ('visa_sponsorship',
         "Enter the visa sponsorship status (True/False, if not specified, enter 'False')"),
        ('job_type',
         "Enter the job type (full-time, part-time, contract, freelance, internship, temporary, or remote) "
         "(if not specified, enter 'Full-time')"),
        ('job_posting_summary',
         "Enter the full job description here, ensuring to fix any grammar errors (if not specified, enter 'None')"),
        ('contact_person_first_name',
         "Enter the first name of the recruiter or hiring manager (if not specified, enter 'None')"),
        ('contact_person_last_name',
         "Enter the last name of the recruiter or hiring manager (if not specified, enter 'None')"),
        ('contact_person_email',
         "Enter the email of the recruiter or hiring manager, not the generic job opening email "
         "(if not specified, enter 'None')"),
        ('contact_person_job_title',
         "Enter the job title of the recruiter or hiring manager (if not specified, enter 'None')"),
        ('contact_person_phone_number',
         "Enter the phone number of the recruiter or hiring manager for this job posting "
         "(if not specified, enter 'None')"),
        ('contact_person_note',
         "Enter a note for the recruiter or hiring manager (if not specified, enter 'None')")
    ]

    return dataset
