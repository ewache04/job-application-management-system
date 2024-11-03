# middleware/subscription_middleware.py

from django.utils.deprecation import MiddlewareMixin
from stripe.error import StripeError
from ManageSubscription.utils.stripe_utils.refund_operations.user_has_requested_refund import user_has_requested_refund
from ManageSubscription.utils.stripe_utils.subscription_operations.retrieve_active_subscription import (
    retrieve_active_subscription)
from ManageSubscription.utils.stripe_utils.subscription_operations.subscription_details import (
    retrieve_or_create_subscription_details)
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI import settings
import stripe


class SubscriptionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user
            stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

            try:
                stripe_customer_id = user.stripe_customer_id
                if not stripe_customer_id:
                    raise ValueError("Stripe customer ID is not set for the user.")

                print(f"Retrieving customer with ID: {stripe_customer_id}")
                customer = stripe.Customer.retrieve(stripe_customer_id)

                # Initialize active_subscription to None
                active_subscription = None

                if not request.session.get('active_subscription') or not request.session.get('all_subscriptions'):
                    active_subscription, all_subscriptions = retrieve_active_subscription(request, stripe_customer_id)
                    create_or_update_session(request, 'active_subscription', active_subscription)
                    create_or_update_session(request, 'all_subscriptions', all_subscriptions)

                if not request.session.get('refund_requested'):
                    user_has_requested_refund(request, user)

                if not request.session.get('my_subscription_detail') and active_subscription:
                    subscription_details = retrieve_or_create_subscription_details(request, active_subscription.id)

                    if isinstance(subscription_details, dict):
                        if 'error' in subscription_details:
                            error_message = subscription_details['error']
                            create_or_update_session(request, 'alert_message', error_message)
                        else:
                            create_or_update_session(request, 'my_subscription_detail', subscription_details)
                    else:
                        raise ValueError("Expected subscription_details to be a dictionary")

            except StripeError as e:
                error_message = e.user_message if e.user_message else str(e)
                print(f"Stripe error: {error_message}")
                create_or_update_session(request, 'alert_message', f'Stripe error: {error_message}')
            except Exception as e:
                print(f"Error: {e}")
                create_or_update_session(request, 'alert_message', f'Error: {e}')
