# ManageSubscription/views/request_subscription_refund/request_subscription_refund.py
import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import redirect

from OpenColabAI import settings
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error


@login_required
def request_subscription_refund(request, user_id, subscription_id):
    user = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    try:
        # Retrieve the subscription
        subscription = stripe.Subscription.retrieve(subscription_id)

        # Get the latest invoice
        latest_invoice_id = subscription.latest_invoice
        invoice = stripe.Invoice.retrieve(latest_invoice_id)

        # Get the charge associated with the invoice
        charge_id = invoice.charge

        # Create a refund
        refund = stripe.Refund.create(
            charge=charge_id
        )

        # Redirect back to the subscription detail with a success message
        print("Refund has been requested successfully.")
        return redirect(urls_paths['subscription_detail']['redirect'],
                        user_id=user.pk, subscription_id=subscription_id)
    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
