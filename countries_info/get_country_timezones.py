# countries_info/get_country_timezones.py
from countries_info import initialize_country_info


def get_country_timezones(name):
    """
    Get the timezones of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - timezones (list): A list of timezones in the country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the timezones of the country
    timezones = country_info.timezones()

    return timezones


# Example usage
# print(get_country_timezones('United States'))
