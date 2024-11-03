import stripe
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from stripe import Customer

from ManageAccounts.forms.user_creation_form.user_creation_form import CustomUserCreationForm
from OpenColabAI import settings
from OpenColabAI.session_utils.create_or_update_sessions import create_or_update_session
from OpenColabAI.settings import urls_paths
from general_utils.greeting_message import greeting_user
from return_to_previous_page import return_to_previous_page


# Create a new user
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()

            # Set the Stripe API key
            stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

            # Create a Stripe customer
            stripe_customer = Customer.create(email=user.email)
            user.stripe_customer_id = stripe_customer.id
            user.save()

            # Log in the user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(f"Signed up as {user.email}")

            greeting = greeting_user(True, user.first_name)

            create_or_update_session(request, 'greeting_message', greeting)
            create_or_update_session(request, 'alert_message',
                                     'Your account has been created successfully. Please log in.')

            return redirect(urls_paths['user_home']['redirect'], user_id=user.pk)
    else:
        form = CustomUserCreationForm()
    context = {
        'urls_paths': urls_paths,
        'user': request.user,
        'form': form,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['signup']['render'], context)
