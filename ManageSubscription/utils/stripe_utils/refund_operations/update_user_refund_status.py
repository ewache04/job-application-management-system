# ManageSubscription/utils/stripe_utils/update_user_refund_status.py
from ManageSubscription.models import UserPayment
from django.core.exceptions import ObjectDoesNotExist

from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session


def update_user_refund_status(request, user, status):
    """
    Set the user's requested refund status in the UserPayment model.

    :param request:
    :param user: The user object whose refund status needs to be updated.
    :param status: The refund status to be set (True or False).
    :return: True if the update was successful, False if the user payment record was not found.
    """
    try:
        user_payment = UserPayment.objects.get(user=user)
        user_payment.refund_requested = status
        user_payment.save()
        status = status
    except ObjectDoesNotExist:
        # Handle the case where the user does not have a payment record
        print(f"No payment record found for user: {user.email}")
        status = status

    finally:
        create_or_update_session(request, 'refund_requested', status)
        return status
