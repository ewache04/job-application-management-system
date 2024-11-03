# countries_info/get_country_name.py
from countries_info import initialize_country_info


def get_country_name(country_code):
    """
    Get the name of a country from its country code.

    Parameters:
    - country_code (str): The country code (ISO 3166-1 alpha-2) of the country.

    Returns:
    - country_name (str): The name of the country.
    """
    try:
        country_info = initialize_country_info(country_code)
        country_name = country_info.name()
        return country_name
    except Exception as e:
        return f"Country not found: {e}"


# Example usage
# print(get_country_name('US'))
