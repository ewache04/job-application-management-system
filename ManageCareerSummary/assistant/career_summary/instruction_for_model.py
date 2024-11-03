# ManageCareerSummary/instructions/instruction_for_career_summary.py

def career_summary_instructions(user=None, job_profiles=None, projects=None):
    """
    Generate structured instructions for creating a career summary.

    Parameters:
    - user: User object containing user information.
    - job_profiles: User's job profile details.
    - projects: User's project details.

    Returns:
    - instruction_script (list): A list of dictionaries representing the career summary instructions.
    """
    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    instruction_script = [
        {"role": "user", "content": "You are a professional career summary writer."},
        {"role": "user", "content": "Based on the provided information, craft a compelling career summary story."},
        {"role": "user", "content": f"User Job Profile: {job_profiles if job_profiles else 'None provided.'}"},
        {"role": "user", "content": f"User Project: {projects if projects else 'None provided.'}"},
        {"role": "user", "content": f"Applicant First Name: {first_name}"},
        {"role": "user", "content": f"Applicant Last Name: {last_name}"},
        {"role": "user", "content": (
            "When providing the 'career_summary', include the following:\n"
            "- Use quantitative metrics where applicable (e.g., number of relevant skills, match percentage with job "
            "roles, quantified achievements).\n"
            "- Provide qualitative insights based on overall impression and specific details.\n"
            "- Make sure you are using the job profile and projects content. Avoid making up information. Instead, "
            "in your story, talk about the provided job profile and project details, and mention the challenges of "
            "crafting a complete career story based on the limited information.\n"
        )},
        {"role": "user", "content": "Thanks! You may generate it now."},
        {"role": "assistant", "content": "Okay."},
    ]

    return instruction_script

# Example usage:
# print(career_summary_instructions())
