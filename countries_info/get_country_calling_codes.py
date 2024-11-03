# countries_info/get_country_calling_codes.py
from countries_info import initialize_country_info


def get_country_calling_codes(name):
    """
    Get the calling codes of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - calling_codes (list): A list of calling codes for the given country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the calling codes of the country
    calling_codes = country_info.calling_codes()

    return calling_codes


# Example usage
print(get_country_calling_codes('France'))
