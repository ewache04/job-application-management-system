# countries_info/get_country_borders.py
from countries_info import initialize_country_info


def get_country_borders(name):
    """
    Get the borders of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - borders (list): A list of countries that share a border with the given country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the borders of the country
    borders = country_info.borders()

    return borders


# Example usage
# print(get_country_borders('France'))
