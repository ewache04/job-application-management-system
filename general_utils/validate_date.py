# general_utils/validate_date.py
from django.utils.dateparse import parse_date


def validate_date(value):
    possible_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%d/%m/%Y', '%B %d, %Y', '%d %B %Y']
    for fmt in possible_formats:
        try:
            parsed_date = parse_date(value.strftime(fmt))
            if parsed_date:
                return parsed_date
        except (ValueError, TypeError):
            continue
    return None
