# ManageJobApplications/resume/instruction_for_model.py
from ManageJobApplications.assistant_operations.resume.resume_extraction_format import resume_extraction_structure


def resume_instructions(user=None, application=None, career_summary=None, raw_resume=None):
    """
    Generate structured instructions for extracting details from a resume.

    Parameters:
    - user: User object containing user information.
    - application: The description of the job posting.
    - work_experience: User's work experience details.
    - raw_resume: User's uploaded resume details.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """
    first_name = user.first_name if user else "First Name"
    last_name = user.last_name if user else "Last Name"

    extraction_structure = resume_extraction_structure()

    instruction_script = [
        {"role": "user", "content": "You are a professional resume analyst."},
        {"role": "user", "content": "Study the data provided below."},
        {"role": "user", "content": f"Job posting details: {application}"},
        {"role": "user", "content": f"Applicant career summary: {career_summary}"},
        {"role": "user", "content": f"Uploaded resume details: {raw_resume}"},
        {"role": "user", "content": f"Applicant first name: {first_name}"},
        {"role": "user", "content": f"Applicant last name: {last_name}"},
        {"role": "user", "content": "Also study the extraction format below. Provide your response in list tuple "
                                    "format."},
        {"role": "user", "content": f"Extraction structure: {extraction_structure}"},
        {"role": "user", "content": (
            "Good format example: [('subject','my subject content goes here. (1,3,4,5,)')]. "
            "Bad format example: [('subject','my subject content goes here. [1,3,4,5,]')]. "
            "Avoid including this kind of error: SyntaxWarning: invalid escape sequence '\\ ', '\\S','\\U','\\D', "
            "'\\A', '\\B', '\\C', '\\E', '\\F', '\\G', '\\H', '\\I', '\\J', '\\K', '\\L', '\\N', '\\O', '\\P', '\\Q', "
            "'\\R', '\\T', '\\V', '\\W', '\\X', '\\Y', '\\Z'."
        )},
        {"role": "user", "content": (
            "When providing the 'assistant_observation', include the following:\n"
            "- Analysis of the resume's structure and format (e.g., layout, readability, use of sections).\n"
            "- Evaluation of the content quality (e.g., clarity, relevance to job description, level of detail).\n"
            "- Identification of strengths (e.g., strong achievements, relevant skills, appropriate keywords).\n"
            "- Identification of weaknesses or areas for improvement (e.g., gaps, irrelevant information, "
            "poor formatting).\n"
            "- Use quantitative metrics where applicable (e.g., number of relevant skills, match percentage with job "
            "description, quantified achievements).\n"
            "- Provide qualitative insights based on overall impression and specific details.\n"
            "- Specific advice on how to improve the resume based on the job description and other provided details.\n"
            "- Ensure the analysis is thorough and provides actionable insights."
        )},
        {"role": "user", "content": (
            "When providing the 'assistant_resume', ensure it incorporates the observational analysis comprehensively. "
            "Address the strengths by emphasizing them and improve on the weaknesses identified in the "
            "'assistant_observation'. Ensure the resume is tailored to the job description and enhances the applicant's"
            "chances of securing the job. Incorporate the following elements:\n"
            "- Enhanced formatting for readability and professional appearance.\n"
            "- Clear and concise language highlighting key qualifications and achievements.\n"
            "- Inclusion of relevant keywords from the job description.\n"
            "- Tailored sections that align with the job requirements and applicant's strengths.\n"
            "- Quantifiable achievements and metrics to demonstrate impact.\n"
            "- Professional summary that effectively highlights the applicant's unique value proposition."
        )},
        {"role": "user", "content": "Thanks! You may generate it now."},
        {"role": "assistant", "content": "Okay."},
    ]

    return instruction_script

# Example usage:
# print(resume_instructions())
