# ManageSubscription/utils/stripe_utils/subscription_operations/get_subscription_details.py
from datetime import datetime, timedelta
import stripe
from django.http import HttpResponse

from ManageSubscription.utils.stripe_utils.refund_operations.refund_period_days import get_refund_period
from OpenColabAI import settings
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST


def fetch_subscription_details(subscription_id):
    """
    Retrieve details of a Stripe subscription and determine refund eligibility.

    :param subscription_id: The ID of the Stripe subscription.
    :return: A dictionary containing subscription details and refund eligibility status.
    """
    try:
        subscription = stripe.Subscription.retrieve(subscription_id)
        subscription_item = subscription['items']['data'][0]
        plan = subscription_item['plan']

        is_active = subscription.status == 'active'

        start_date = datetime.fromtimestamp(subscription.start_date)
        current_date = datetime.now()
        refund_eligible = is_active and (current_date - start_date <= timedelta(days=get_refund_period()))

        next_billing_date = datetime.fromtimestamp(subscription.current_period_end).strftime('%Y-%m-%d')

        subscription_details = {
            'plan_nickname': plan.nickname,
            'status': subscription.status,
            'amount': plan.amount / 100,  # Convert cents to dollars
            'currency': plan.currency.upper(),
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': datetime.fromtimestamp(subscription.current_period_end).strftime('%Y-%m-%d'),
            'next_billing_date': next_billing_date,
            'interval': plan.interval,
            'id': subscription.id,
            'subscription': subscription,
            'refund_eligible': refund_eligible
        }

        return subscription_details
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e.user_message if e.user_message else e}")
        return {'error': str(e)}
    except Exception as e:
        print(f"General error: {e}")
        return {'error': str(e)}


def retrieve_or_create_subscription_details(request, subscription_id):
    """
    Retrieve subscription details from the session or fetch from Stripe if not available in the session.

    :param request: The HTTP request object.
    :param subscription_id: The ID of the Stripe subscription.
    :return: The subscription details dictionary or an error dictionary.
    """
    subscription_details = request.session.get('subscription_details', None)
    if not subscription_details:
        subscription_details = fetch_subscription_details(subscription_id)
        if 'error' in subscription_details:
            return subscription_details  # Return error dictionary
        create_or_update_session(request, 'subscription_details', subscription_details)
    return subscription_details


