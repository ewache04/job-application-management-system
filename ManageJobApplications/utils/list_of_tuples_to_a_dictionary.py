def list_of_tuples_to_a_dictionary(data):
    """
    Convert a list of tuples to a dictionary.

    Parameters:
    - data (list of tuples): The list of tuples to be converted.

    Returns:
    - dict: The dictionary created from the list of tuples.
    """
    application_data = {key: value for key, value in data}
    return application_data
