# ManageSubscription/utils/get_refund_period.py
def get_refund_period(default_days=2):
    """
    Returns the refund period in days.
    This function can be extended to retrieve the period from a configuration file or environment variable.

    :param default_days: The default number of days for the refund period.
    :return: The number of days for the refund period.
    """
    # Future enhancement: Fetch the refund period from a configuration file or environment variable
    return default_days
