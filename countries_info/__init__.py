# countries_info/__init__.py

# Import the required module
import pycountry
from countryinfo import CountryInfo


def initialize_country_info(name=None):
    """
    Initialize and return a CountryInfo instance for the given country name.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - country_info (CountryInfo): An instance of the CountryInfo class.
    """
    return CountryInfo(name)


def initialize_py_country(name=None):
    """
    Initialize and return a pycountry database instance.

    Parameters:
    - name (str): The name of the country (optional).

    Returns:
    - py_country (pycountry.database): An instance of the pycountry database.
    """
    return pycountry
