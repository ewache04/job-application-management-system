# ManageSubscription/urls.py
"""
URL configuration for ManageSubscription app.

The `initialize_urlpatterns` function initializes URL patterns for the ManageSubscription app.

"""


def initialize_urlpatterns():
    """
    Initialize URL patterns for the ManageSubscription app.

    Returns:
        list: List of URL patterns.
    """
    from ManageSubscription.urls.stripe.stripe_subscription_urlpatterns import get_stripe_subscription_urlpatterns

    print("Initializing ManageSubscription URL patterns")

    urlpatterns = []

    # Add subscription URL patterns
    urlpatterns += get_stripe_subscription_urlpatterns()

    print("Completed initializing URL patterns")

    return urlpatterns
