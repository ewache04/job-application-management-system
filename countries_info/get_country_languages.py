# countries_info/get_country_languages.py

from countries_info import initialize_py_country, initialize_country_info


def get_language_name(language_code):
    """
    Get the full name of a language from its ISO 639-1 language code.

    Parameters:
    - language_code (str): The ISO 639-1 language code.

    Returns:
    - language_name (str): The full name of the language.
    """
    try:
        language = initialize_py_country().languages.get(alpha_2=language_code)
        if language:
            return language.name
        else:
            return "Language not found"
    except AttributeError:
        return "Language code not valid"


def get_country_languages(name):
    """
    Get the languages spoken in a country.

    Parameters:
    - name (str): The name of the country.

    Returns:
    - languages (list): A list of languages spoken in the country.
    """
    try:
        # Initialize CountryInfo for the given country name
        country_info = initialize_country_info(name)

        # Get the language codes spoken in the country
        language_codes = country_info.languages()

        # Get the full names of the languages
        languages = [get_language_name(code) for code in language_codes]

        return languages

    except KeyError:

        # Handle the case where the country name is not found
        return [f'Language information not found for {name}']

# Example usage
# print(get_country_languages('Andorra'))
