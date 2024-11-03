# ManageJobApplications/cover_letter_extraction_structure.py

def cover_letter_extraction_structure():
    """
    Return the expected structure for extracting cover letter details.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected structure.
    """
    dataset = [
        ('subject', "Enter the cover letter subject here"),
        ('letter', "Enter the cover letter message here. Ensure the cover letter includes the following components:\n"
                   "- Salutation addressing the hiring manager or recruiter by name, if possible.\n"
                   "- Introduction expressing enthusiasm for the opportunity and interest in the position.\n"
                   "- Brief overview of qualifications and experiences relevant to the job.\n"
                   "- Highlighting specific achievements or skills that demonstrate suitability for the role.\n"
                   "- Alignment of experience with the job requirements and company culture.\n"
                   "- Customization based on the job description and company research.\n"
                   "- Closing expressing appreciation for consideration and willingness to discuss further.\n"
                   "- Professional sign-off with full name and contact information."),
        ('assistant_observation', "Enter the assistant observation here. This should include an analysis of the cover "
                                  "letter's structure, content quality, strengths, weaknesses, and specific advice for"
                                  "improvement.")
    ]

    return dataset
