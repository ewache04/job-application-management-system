# ManageSubscription/utils/stripe_utils/user_has_requested_refund.py
import stripe
from ManageSubscription.utils.stripe_utils.refund_operations.update_user_payment_status import \
    update_user_payment_status
from ManageSubscription.utils.stripe_utils.refund_operations.update_user_refund_status import update_user_refund_status
from OpenColabAI import settings
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

stripe.api_key = settings.STRIPE_SECRET_KEY_TEST


def user_has_requested_refund(request, user):
    """
    Check if the user has requested a refund in Stripe.

    :param request: The HTTP request object.
    :param user: The user object.
    :return: True if the user has requested a refund, False otherwise.
    """
    try:
        charges = stripe.Charge.list(customer=user.stripe_customer_id)

        if charges.data:
            sorted_charges = sorted(charges.data, key=lambda x: x.created, reverse=True)
            most_recent_charge = sorted_charges[0]

            user_requested_refund = most_recent_charge.amount_refunded > 0

            create_or_update_session(request, 'refund_requested', user_requested_refund)
            update_user_refund_status(request, user, user_requested_refund)
            update_user_payment_status(user)

            return user_requested_refund

        create_or_update_session(request, 'refund_requested', False)
        update_user_refund_status(request, user, False)
        update_user_payment_status(user)

        return False
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e.user_message if e.user_message else e}")
    except Exception as e:
        print(f"General error: {e}")

    update_user_refund_status(request, user, False)
    return False

