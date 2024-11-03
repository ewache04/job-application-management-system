# ManageJobApplications/resume/resume_extraction_format.py

def resume_extraction_structure():
    """
    Define the expected structure for extracting resume details.

    Returns:
    - structure (list of tuples): A list of tuples representing the expected resume structure.
    """
    dataset = [
        ('resume_name', "You must enter the applicant's full name here. If not found, enter 'None'."),
        ('resume_email', "You must enter the applicant's email address here. If not found, enter 'None'."),
        ('assistant_observation', "You must provide an assistant observational analysis that advises the applicant "
                                  "based on the submitted resume in relation to the job description and other "
                                  "provided details. Include a detailed analysis highlighting both strengths and "
                                  "areas for improvement. Utilize both qualitative and quantitative metrics. "
                                  "If not found, enter 'None'."),
        ('assistant_resume', "You must provide a recommended assistant-generated resume here. Incorporate the "
                             "observational analysis to enhance this version, addressing the identified strengths "
                             "and areas for improvement. The resume should be tailored to the job description "
                             "and significantly improve the applicant's chances of securing the job. "
                             "If not found, enter 'None'."),
    ]

    return dataset

# Example usage:
# print(resume_extraction_structure())
