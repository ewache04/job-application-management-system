# countries_info/get_country_capital.py
from countries_info import initialize_country_info


def get_country_capital(name):
    """
    Get the capital of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - capital (str): The capital city of the country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the capital of the country
    capital = country_info.capital()

    return capital


# Example usage
# print(get_country_capital('France'))
