# ManageSubscription/views/subscription_detail/subscription_detail.py

from datetime import datetime, timedelta
import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render

from ManageSubscription.utils.stripe_utils.subscription_operations.subscription_details import \
    retrieve_or_create_subscription_details
from OpenColabAI import settings
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def subscription_detail(request, user_id, subscription_id):
    user = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    try:
        subscription_details = retrieve_or_create_subscription_details(request, subscription_id)
        if isinstance(subscription_details, HttpResponse):
            return subscription_details

        context = {
            'subscription_detail': subscription_details,
            'urls_paths': urls_paths,
            'refund_eligible': subscription_details.get('refund_eligible'),
            'user': user,
            'subscription': subscription_details.get('subscription'),
            'content_details_mode': True,
            'stripe_subscription_details_mode': True,
            'return_to_previous_page': return_to_previous_page,
        }

        return render(request, urls_paths['subscription_detail']['render'], context)
    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred. Please try again later. {str(e)}")
