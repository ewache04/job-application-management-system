# countries_info/get_country_population.py
from countries_info import initialize_country_info


def get_country_population(name):
    """
    Get the population of a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - population (int): The population of the country.
    """
    # Initialize CountryInfo for the given country name
    country_info = initialize_country_info(name)

    # Get the population of the country
    population = country_info.population()

    return population

# Example usage
# print(get_country_population('France'))
