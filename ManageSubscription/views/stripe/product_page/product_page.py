# ManageSubscription/views/product_page/product_page.py
import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from ManageSubscription.products.stripe.products import products_type
from OpenColabAI import settings
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


@login_required
def product_page(request, user_id, subscription_id=None):
    user = request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    if request.method == 'POST':
        try:
            # Fetch the product to check if it is active
            price = stripe.Price.retrieve(settings.PRODUCT_PRICE_ID)
            product = stripe.Product.retrieve(price.product)

            if not product.active:
                return HttpResponse("Error: The product is not active.", status=400)

            # Ensure the user has a Stripe customer ID
            if not hasattr(user, 'stripe_customer_id') or not user.stripe_customer_id:
                customer = stripe.Customer.create(email=user.email)
                user.stripe_customer_id = customer.id
                user.save()
            else:
                customer = stripe.Customer.retrieve(user.stripe_customer_id)

            # Create the checkout session
            checkout_session = stripe.checkout.Session.create(
                customer=customer.id,
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': settings.PRODUCT_PRICE_ID,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=f"{settings.REDIRECT_DOMAIN}/user/{user_id}/payment_successful?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"{settings.REDIRECT_DOMAIN}/payment_cancelled/",
            )

            return redirect(checkout_session.url, code=303)
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=500)

    # Retrieve the product and pricing information from Stripe
    try:
        product_price = stripe.Price.retrieve(settings.PRODUCT_PRICE_ID)
        product_amount = product_price.unit_amount / 100  # Convert amount from cents to dollars
        product_currency = product_price.currency.upper()
        product_id = product_price.product
        product_details = stripe.Product.retrieve(product_id)
        product_name = product_details.name
        product_description = product_details.description

    except Exception as e:
        return HttpResponse(f"Error retrieving product price: {e}", status=500)

    # Define the products with features
    products = products_type(name=product_name, price=product_amount, currency=product_currency,
                             description=product_description)

    context = {
        'user': user,
        'products': products,
        'urls_paths': urls_paths,
        'return_to_previous_page': return_to_previous_page,
    }

    return render(request, urls_paths['product_page']['render'], context)