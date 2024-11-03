# countries_info/get_country_area.py
from countries_info import initialize_country_info


def get_country_area(name):
    """
    Get the area of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - area (float): The area of the country in square kilometers.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the area of the country
    area = country_info.area()

    return area


# Example usage
# print(get_country_area('France'))
