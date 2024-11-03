# countries_info/get_country_provinces.py
from countries_info import initialize_country_info


def get_country_provinces(name):
    """
    Get the provinces or states of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - provinces (list): A list of provinces or states in the country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the provinces of the country
    provinces = country_info.provinces()

    return provinces


# Example usage
# print(get_country_provinces('United States'))
