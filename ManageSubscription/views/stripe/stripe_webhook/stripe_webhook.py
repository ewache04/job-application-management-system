# ManageSubscription/views/stripe_webhook/stripe_webhook.py
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ManageJobApplications.utils.thread_delay import thread_delay
from ManageSubscription.models import UserPayment
from OpenColabAI import settings


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    thread_delay(10)

    payload = request.body
    signature_header = request.META.get('HTTP_STRIPE_SIGNATURE', None)

    if not signature_header:
        return HttpResponse("Missing signature", status=400)

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)

        thread_delay(15)

        try:
            user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
            user_payment.payment_bool = True
            user_payment.save()
        except UserPayment.DoesNotExist:
            return HttpResponse("Payment record not found", status=404)

    return HttpResponse(status=200)
