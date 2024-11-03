# ManageSubscription/urls/subscription_urlpatterns.py
from django.urls import path


def get_stripe_subscription_urlpatterns():
    from ManageSubscription.views.stripe.manage_stripe_subscription import manage_stripe_subscription
    from ManageSubscription.views.stripe.payment_cancelled import payment_cancelled
    from ManageSubscription.views.stripe.payment_successful import payment_successful
    from ManageSubscription.views.stripe.product_page import product_page
    from ManageSubscription.views.stripe.stripe_webhook import stripe_webhook
    from ManageSubscription.views.stripe.subscription_detail import subscription_detail
    from ManageSubscription.views.stripe.subscription_list import subscription_list

    print("Initializing subscription URL patterns")

    subscription_urlpatterns = [
        path('user/<int:user_id>/product_page/',
             product_page.product_page, name='product_page'),

        path('user/<int:user_id>/manage_stripe_subscription/<str:subscription_id>/',
             manage_stripe_subscription.manage_stripe_subscription, name='manage_stripe_subscription'),

        path('user/<int:user_id>/subscription_list/',
             subscription_list.subscription_list, name='subscription_list'),

        path('user/<int:user_id>/subscription_detail/<str:subscription_id>/',
             subscription_detail.subscription_detail,
             name='subscription_detail'),

        path('stripe_webhook/',
             stripe_webhook.stripe_webhook, name='stripe_webhook'),

        path('user/<int:user_id>/payment_successful/',
             payment_successful.payment_successful,
             name='payment_successful'),

        path('user/<int:user_id>/payment_cancelled/',
             payment_cancelled.payment_cancelled,
             name='payment_cancelled'),
    ]

    print("Completed initializing subscription URL patterns")

    return subscription_urlpatterns
