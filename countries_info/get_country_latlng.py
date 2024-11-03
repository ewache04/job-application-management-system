# countries_info/get_country_latlng.py
from countries_info import initialize_country_info


def get_country_capital_latlng(name):
    """
    Get the latitude and longitude of a country's capital.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - capital_latlng (tuple): A tuple containing the latitude and longitude of the capital city.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the capital's latitude and longitude
    capital_latlng = country_info.capital_latlng()

    return capital_latlng

# Example usage
# print(get_country_capital_latlng('France'))

