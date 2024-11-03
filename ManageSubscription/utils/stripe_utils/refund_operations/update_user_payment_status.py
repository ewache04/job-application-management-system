# ManageSubscription/utils/stripe_utils/update_user_payment_status.py
from ManageSubscription.models import UserPayment
from django.core.exceptions import ObjectDoesNotExist


def update_user_payment_status(user):
    """
    Update the payment status (payment_bool) in the UserPayment model for a given user.
    If refund_requested is True, set payment_bool to False and vice versa.

    :param user: The user object whose payment status needs to be updated.
    :return: True if the update was successful, False if the user payment record was not found.
    """
    try:
        user_payment = UserPayment.objects.get(user=user)
        user_payment.payment_bool = not user_payment.refund_requested
        user_payment.save()
        return True
    except ObjectDoesNotExist:
        # Handle the case where the user does not have a payment record
        return False
