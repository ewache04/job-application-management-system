# countries_info/country_list.py
import pycountry


def get_country_list():
    # Get a list of country names from pycountry
    countries = list(pycountry.countries)

    # Create a list of tuples containing country code and country name
    country_choices = [(country.name, country.name) for country in countries]

    # Sort the list of tuples alphabetically based on country names
    sorted_country_choices = sorted(country_choices, key=lambda x: x[1])

    return sorted_country_choices
