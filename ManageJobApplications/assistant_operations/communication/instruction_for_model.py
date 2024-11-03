# ManageJobApplications/communication/instruction_for_model.py
from django.http import request

from ManageJobApplications.assistant_operations.applications.job_description_extraction_output_structure_format import \
    job_extraction_structure
from ManageJobApplications.assistant_operations.communication.communication_extraction_format import \
    communication_extraction_structure


def communication_instructions(user=None, company_message=None, applicant_message=None):
    """
    Generate structured instructions for extracting details from a communication between a company and an applicant.

    Parameters:
    - user: User object containing user information.
    - company_message (str): The message from the company.
    - applicant_message (str): The message from the applicant.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """
    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    extraction_structure = communication_extraction_structure()

    instruction_script = [
        {
            "role": "user",
            "content": (
                "You are an expert in analyzing and extracting details from communications between companies and job "
                "applicants."
                "I will provide you with a series of messages exchanged between a company and an applicant. "
                "Your task is to extract and analyze these messages, and summarize them in a structured format."
            )
        },
        {
            "role": "user",
            "content": (
                "Here are the specific tasks you need to perform: "
                "1. Extract the company message. "
                "2. Extract the applicant's message. "
                "3. Create a detailed summary of both communications in a coherent narrative. "
                "4. Perform an analysis of the interaction, highlighting the key points and tone of each message."
            )
        },
        {
            "role": "user",
            "content": f"Company message details: {company_message if company_message else 'None provided.'}"
        },
        {
            "role": "user",
            "content": f"Applicant message details: {applicant_message if applicant_message else 'None provided.'}"
        },
        {
            "role": "user",
            "content": f"Applicant first name: {first_name}"
        },
        {
            "role": "user",
            "content": f"Applicant last name: {last_name}"
        },
        {
            "role": "user",
            "content": (
                "Use the following format for your response. Ensure you adhere strictly to this format, as it is "
                "crucial for the integrity of our program."
                "Each item should be enclosed in square brackets, and the structure should be as follows: "
                f"{extraction_structure}. "
                "Make sure the summary is between 1000 and 1440 tokens long. "
                "For listing items, use the format: (e.g., 1, 3, 4, 5). "
                "Avoid using decorative characters such as ** or \\n, as these will disrupt the template display. "
                "Good example: [('communication_subject', 'Provide a short and concise subject. (1, 3, 4, 5,)')]. "
                "Bad example: [('communication_subject', 'Provide a concise subject [1, 3, 4, 5,]')]. "
                "Do not include invalid escape sequences like '\\ ', '\\S', '\\U', etc."
            )
        },
        {
            "role": "user",
            "content": (
                "If any information such as the company message, applicant message, or applicant's name is missing, "
                "indicate 'None' or create a plausible communication based on the provided information."
            )
        },
        {
            "role": "user",
            "content": "Thank you. Please proceed with generating the analysis."
        },
        {
            "role": "assistant",
            "content": "Understood."
        },
    ]

    return instruction_script

# Example usage:
# print(communication_instructions())
