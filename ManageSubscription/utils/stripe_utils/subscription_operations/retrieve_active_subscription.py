# ManageSubscription/utils/stripe_utils/retrieve_active_subscription.py
import stripe
from OpenColabAI import settings
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST


def retrieve_active_subscription(request, stripe_customer_id):
    try:
        if not stripe_customer_id:
            raise ValueError("Stripe customer ID is required.")

        subscriptions = stripe.Subscription.list(customer=stripe_customer_id)
        if not subscriptions.data:
            print(f"No subscriptions found for customer ID: {stripe_customer_id}")
            create_or_update_session(request, 'all_subscriptions', subscriptions)
            create_or_update_session(request, 'subscription_active', None)
            return None, subscriptions

        active_subscription = next((sub for sub in subscriptions.data if sub.status == 'active'), None)
        create_or_update_session(request, 'all_subscriptions', subscriptions)
        create_or_update_session(request, 'subscription_active', active_subscription)

        return active_subscription, subscriptions
    except stripe.error.InvalidRequestError as e:
        print(f"Invalid request error: {e.user_message}")
        raise ValueError(f"Invalid request error: {e.user_message}")
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e.user_message}")
        raise ValueError(f"Stripe error: {e.user_message}")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise ValueError(f"An error occurred: {e}")

