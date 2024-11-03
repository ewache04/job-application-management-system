from ManageJobApplications.utils.list_of_tuples_to_a_dictionary import list_of_tuples_to_a_dictionary
from general_utils.get_horizontal_line import get_horizontal_line


def convert_to_form_data(data):
    """
    Convert the given data to form data format.

    Parameters:
    - data (list of tuples): The data to be converted.

    Returns:
    - form_data (dict): The converted data in dictionary format, or None if input is invalid.
    """

    if data is not None:
        # Convert the list of tuples to a dictionary
        form_data = list_of_tuples_to_a_dictionary(data)
        get_horizontal_line()
        return form_data
    else:
        return None
