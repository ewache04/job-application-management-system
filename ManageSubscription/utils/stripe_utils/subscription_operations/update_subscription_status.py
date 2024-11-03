# ManageSubscription/utils/stripe_utils/update_subscription_status.py
from ManageSubscription.models import UserPayment
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session

def update_subscription_status(request, user, subscription_active):
    """
    Retrieve and update the subscription status in the session if it has changed.

    :param subscription_active: Boolean indicating if the subscription is active.
    :param request: The HTTP request object.
    :param user: The user object.
    :return: The current subscription status.
    """
    # Update user payment model accordingly
    try:
        subscription_active = bool(subscription_active)

        print(f'subscription_active: {subscription_active}')
        user_payment = UserPayment.objects.get(user=user)
        user_payment.subscription_active = subscription_active
        user_payment.save()

        # Update the session with the new subscription status
        create_or_update_session(request, 'subscription_active', subscription_active)
        print(f'Updated subscription status for user: {user.email} to {subscription_active}')

    except UserPayment.DoesNotExist:
        print(f"No payment record for user: {user.email}")

    except Exception as e:
        print(f"An error occurred while updating subscription status for user: {user.email}. Error: {str(e)}")
