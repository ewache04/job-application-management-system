# ManageSubscription/views/manage_subscription/manage_subscription.py

import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect

from ManageSubscription.models import UserPayment
from ManageSubscription.utils.stripe_utils.refund_operations.update_user_payment_status import update_user_payment_status
from ManageSubscription.utils.stripe_utils.refund_operations.update_user_refund_status import update_user_refund_status
from ManageSubscription.utils.stripe_utils.refund_operations.user_has_requested_refund import user_has_requested_refund
from ManageSubscription.utils.stripe_utils.subscription_operations.subscription_details import fetch_subscription_details, retrieve_or_create_subscription_details
from ManageSubscription.utils.stripe_utils.subscription_operations.update_subscription_status import update_subscription_status
from OpenColabAI import settings
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.error_logging import log_error
from return_to_previous_page import return_to_previous_page


@login_required
def manage_stripe_subscription(request, user_id, subscription_id):
    user = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    user_payment = UserPayment.objects.get(user=user)

    try:
        if not hasattr(user, 'stripe_customer_id') or not user.stripe_customer_id:
            customer = stripe.Customer.create(email=user.email)
            user.stripe_customer_id = customer.id
            user.save()
            print(f'Stripe customer created successfully for user: {user.email}')

        if request.method == 'POST':
            action = request.POST.get('action')
            subscription_id = request.POST.get('subscription_id')

            if action and subscription_id:
                subscription = stripe.Subscription.retrieve(subscription_id)

                if action == 'cancel':
                    stripe.Subscription.modify(subscription_id, cancel_at_period_end=True)
                    update_subscription_status(request, user, False)
                    create_or_update_session(request, 'alert_message', 'Subscription successfully canceled.')
                    return redirect(urls_paths['subscription_list']['redirect'], user_id=user.pk)

                elif action == 'resume':
                    stripe.Subscription.modify(subscription_id, cancel_at_period_end=False)
                    update_subscription_status(request, user, True)
                    create_or_update_session(request, 'alert_message', 'Subscription successfully resumed.')
                    return redirect(urls_paths['subscription_list']['redirect'], user_id=user.pk)

                elif action == 'refund':
                    if not user_payment.refund_requested:
                        latest_invoice_id = subscription.latest_invoice
                        invoice = stripe.Invoice.retrieve(latest_invoice_id)
                        charge_id = invoice.charge
                        refund = stripe.Refund.create(charge=charge_id)

                        if refund.status == 'succeeded':
                            update_user_refund_status(request, user, True)
                            update_user_payment_status(user)
                            create_or_update_session(request, 'alert_message', 'Refund successfully initiated.')
                            return redirect(urls_paths['subscription_list']['redirect'], user_id=user.pk)
                        else:
                            create_or_update_session(request, 'alert_message', 'Failed to initiate refund.')
                            return redirect(urls_paths['manage_stripe_subscription']['redirect'], user_id=user.pk, subscription_id=subscription.id)
                    else:
                        create_or_update_session(request, 'alert_message', 'Refund request already made.')
                        return redirect(urls_paths['manage_stripe_subscription']['redirect'], user_id=user.pk, subscription_id=subscription.id)
                else:
                    return HttpResponse("Invalid action.", status=400)
            else:
                return HttpResponse("Action or subscription ID not provided.", status=400)

        subscription_details = retrieve_or_create_subscription_details(request, subscription_id)
        if isinstance(subscription_details, HttpResponse):
            return subscription_details

        refund_requested = user_has_requested_refund(request, user)

        context = {
            'urls_paths': urls_paths,
            'user': user,
            'my_subscription_detail': subscription_details,
            'next_billing_date': subscription_details.get('next_billing_date'),
            'refund_eligible': subscription_details.get('refund_eligible'),
            'refund_requested': refund_requested,
            'subscription_active': user_payment.subscription_active,
            'return_to_previous_page': return_to_previous_page,
            'subscription': subscription_details.get('subscription'),
            'content_details_mode': True,
            'manage_stripe_subscription_mode': True,
        }
        print(f"subscription_active: {user_payment.subscription_active}")

        return render(request, urls_paths['manage_stripe_subscription']['render'], context)

    except stripe.error.InvalidRequestError as e:
        create_or_update_session(request, 'alert_message', f'Request error: {e}')
        log_error(f'Stripe error while checking readability: {e}')
        print(e)
        return redirect(urls_paths['manage_stripe_subscription']['redirect'], user_id=user.pk, subscription_id=subscription_id)

    except stripe.error.StripeError as e:
        create_or_update_session(request, 'alert_message', f'Stripe error: {e}')
        log_error(f'Stripe error while checking readability: {e}')
        return redirect(urls_paths['manage_stripe_subscription']['redirect'], user_id=user.pk, subscription_id=subscription_id)

    except Exception as e:
        log_error(f'Error managing subscription for user {user.email}: {e}')
        return HttpResponseServerError(f"Error: {e}")
