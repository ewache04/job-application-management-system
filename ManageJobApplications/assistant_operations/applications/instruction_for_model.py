# ManageJobApplications/instruction_for_model.py
from ManageJobApplications.assistant_operations.applications.job_description_extraction_output_structure_format import \
    job_extraction_structure


def job_description_extraction_instructions(job_description):
    """
    Generate structured instructions for extracting details from a job description.

    Parameters:
    - job_description (str): The description of the job posting.

    Returns:
    - instruction_script (list): A list of dictionaries representing the extraction instructions.
    """

    extraction_structure = job_extraction_structure()

    instruction_script = [

        {"role": "user", "content": "I need your help extracting details from this job description."},
        {"role": "assistant", "content": "Sure thing! Please provide the job description."},
        {"role": "user", "content": f"Here is the job description: {job_description}"},
        {"role": "assistant", "content": "Thank you. I'll now extract the important details:"},
        {"role": "user", "content": f"Here is the format for the assistant's response. Use square brackets as "
                                    f"indicated. Anything other than this will break my program flow: "
                                    f"{extraction_structure}. "
                                    "For listing items, use the format: (put items in here, e.g., 1,3,4,5). "
                                    "Do not include decorative characters such as ** or \\n, as I will display it in "
                                    "the template."
                                    "Good format: [('subject','my subject content goes here. (1,3,4,5,)')]. "
                                    "Bad format: [('subject','my subject content goes here. [1,3,4,5,]')]. "
                                    "Avoid invalid escape sequences: '\\ ', '\\S', '\\U', '\\D', '\\T', '\\L', '\\A', "
                                    "'\\B', '\\C', '\\E',"
                                    "'\\F', '\\G', '\\H', '\\I', '\\J', '\\K', '\\N', '\\O', '\\P', '\\Q', '\\R', "
                                    "'\\V', '\\W', '\\X',"
                                    "'\\Y', '\\Z', '\\[', '\\]', '\\^', '\\_', '\\`', '\\a', '\\b', '\\c', '\\e', "
                                    "'\\f', '\\g', '\\h',"
                                    "'\\i', '\\j', '\\k', '\\l', '\\m', '\\o', '\\p', '\\q', '\\r', '\\s', '\\t', "
                                    "'\\u', '\\v',"
                                    "'\\w', '\\x', '\\y', '\\z'"
         },
        {"role": "user", "content": "Thanks! You may generate it now."},
        {"role": "assistant", "content": "Okay."},
    ]

    return instruction_script
