# countries_info/get_country_alt_spellings.py

# Importing the initialization function for accessing CountryInfo
from countries_info import initialize_country_info


def get_country_alt_spellings(name):
    """
    Get the alternative spellings of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - alt_spellings (list): List of alternative spellings of the country.
    """
    # Initialize CountryInfo for the given country name
    country = initialize_country_info(name)

    # Get the alternative spellings of the country
    alt_spellings = country.alt_spellings()

    return alt_spellings
