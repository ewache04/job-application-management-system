# countries_info/get_country_currencies.py
from countries_info import initialize_country_info


def get_country_currencies(name):
    """
    Get the currencies used in a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - currencies (list): A list of currencies used in the country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the currencies used in the country
    currencies = country_info.currencies()

    return currencies


# Example usage
# print(get_country_currencies('France'))
