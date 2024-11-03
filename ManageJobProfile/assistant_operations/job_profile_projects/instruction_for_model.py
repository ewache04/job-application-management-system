# ManageJobApplications/communication/instruction_for_model.py
from ManageJobProfile.assistant_operations.job_profile_projects.job_profile_projects_extraction_format import \
    job_profile_project_extraction_structure


def job_profile_projects_instructions(user=None, project_text=None):
    """
    Generate structured instructions for extracting details from job profile projects.

    Parameters:
    - user: User object containing user information.
    - project_text (str): The text containing details of the project.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """
    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    extraction_structure = job_profile_project_extraction_structure()

    instruction_script = [
        {
            "role": "user",
            "content": (
                "You are an expert in extracting relevant details from projects done by an applicant. "
                "I will provide you with a text, and you will extract and summarize the project into bullet points. "
                "You must ensure to phrase it so it can be useful for resumes, cover letters, follow-up messages, etc."
            )
        },
        {
            "role": "user",
            "content": (
                "Here are the specific tasks you need to perform: "
                "1. Extract the relevant details from projects done by an applicant. "
                "2. Create a detailed summary of each project, ensuring it is in bullet points. "
                "3. Make the summaries clear and straight to the point."
            )
        },
        {
            "role": "user",
            "content": f"Project message details: {project_text if project_text else 'None provided.'}"
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
                "crucial for the integrity of our program. "
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
                "If any information such as the project details or applicant's name is missing, "
                "indicate 'None' or create a plausible summary based on the provided information."
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
# print(job_profile_projects_instructions())
