# ManageJobApplications/follow_up_extraction_structure.py

def follow_up_extraction_structure():
    """
    Return the expected structure for extracting follow-up message details.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected structure.
    """
    dataset = [
        ('follow_up_message_subject', "Enter the follow-up message subject here"),
        ('follow_up_message', "Enter the follow-up message content here. Include the following components:\n"
                              "- Introduction expressing gratitude for the opportunity to apply and interest in the "
                              "position.\n"
                              "- Brief recap of qualifications and experiences relevant to the job.\n"
                              "- Mention of any specific achievements or skills that make the applicant a strong "
                              "fit.\n"
                              "- Express enthusiasm for the opportunity to contribute to the company.\n"
                              "- Polite request for an update on the application status or next steps.\n"
                              "- Professional closing expressing appreciation for the hiring manager's time and "
                              "consideration.")
    ]

    # Return the list of tuples
    return dataset

# Example usage:
# print(follow_up_extraction_structure())
