# ManageSubscription/views/subscription_list/subscription_list.py
from datetime import datetime

import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.shortcuts import render

from OpenColabAI import settings
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def subscription_list(request, user_id):
    try:
        user = request.user
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

        # Retrieve all the user's subscriptions
        subscriptions = stripe.Subscription.list(customer=user.stripe_customer_id)

        # Extract relevant details from subscriptions data
        subscription_details = []
        subscription_active = False
        for subscription in subscriptions.data:
            if subscription['items']['data']:
                item = subscription['items']['data'][0]  # Assuming there's at least one item

                details = {
                    'id': subscription.id,
                    'plan_nickname': item['plan']['nickname'],
                    'status': subscription.status,
                    'amount': item['plan']['amount'] / 100,  # Assuming the amount is in cents
                    'currency': item['plan']['currency'].upper(),
                    'start_date': datetime.fromtimestamp(subscription.start_date).strftime('%Y-%m-%d'),
                    'end_date': datetime.fromtimestamp(subscription.current_period_end).strftime('%Y-%m-%d'),
                }
                subscription_details.append(details)
                if subscription.status == 'active':
                    subscription_active = True

        context = {
            'all_subscription_details': subscription_details,
            'subscription_active': subscription_active,
            'urls_paths': urls_paths,
            'user': user,
            'return_to_previous_page': return_to_previous_page,
            'search_table': True,
            'list_display_mode': True,
            'stripe_subscription_list_mode': True,
        }

        return render(request, urls_paths['subscription_list']['render'], context)
    except stripe.error.StripeError as e:
        log_error(f"Stripe error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred with Stripe. Please try again later. {str(e)}")
    except Exception as e:
        log_error(f"An unexpected error occurred: {str(e)}")
        return HttpResponseServerError(f"An unexpected error occurred. Please try again later. {str(e)}")