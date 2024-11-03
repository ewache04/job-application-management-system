# In ManageSubscription/views/payment_successful/payment_successful.py
import datetime

import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.utils import timezone

from ManageSubscription.models import UserPayment
from OpenColabAI import settings
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def payment_successful(request, user_id):
    user = request.user
    if user.id != user_id:
        return HttpResponseServerError("Unauthorized access.")

    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('session_id', None)

    if not checkout_session_id:
        return HttpResponse("Missing session ID", status=400)

    checkout_session_id = checkout_session_id.strip().rstrip('/')

    try:
        checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)
        subscription_id = checkout_session.subscription
        session_amount_total = checkout_session.amount_total
        customer_email = checkout_session.customer_details.email
        transaction_date = datetime.datetime.fromtimestamp(checkout_session.created, tz=timezone.utc)

        subscription = stripe.Subscription.retrieve(subscription_id)
        product_name = subscription['items']['data'][0]['plan']['nickname']
        expiration_date = datetime.datetime.fromtimestamp(subscription.current_period_end, tz=timezone.utc)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'session_id': checkout_session_id,
            'subscription_id': subscription.id,
            'subscription': subscription,
            'return_to_previous_page': return_to_previous_page,
            'session_amount_total': session_amount_total / 100,  # convert cents to dollars
            'customer_email': customer_email,
            'transaction_date': transaction_date,
            'amount_paid': session_amount_total / 100,  # convert cents to dollars
            'product_name': product_name,
            'transaction_id': checkout_session.payment_intent,
            'expiration_date': expiration_date,
        }

        # Update the UserPayment instance with the new data
        user_payment, created = UserPayment.objects.get_or_create(user=user)
        user_payment.payment_bool = True
        user_payment.stripe_checkout_id = checkout_session_id
        user_payment.save()

        return render(request, urls_paths['payment_successful']['render'], context)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
