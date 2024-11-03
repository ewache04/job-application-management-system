# ManageAccounts/views/password/forgotten_password_recovery/password_reset_email.py
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

from ManageAccounts.forms.password.forgotten_password_recovery.password_reset_email_form import CustomPasswordResetForm
from OpenColabAI.settings import urls_paths
from return_to_previous_page import return_to_previous_page


def password_reset_email(request):
    user = None
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            associated_users = get_user_model().objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = urls_paths['password_reset_email_message']['render']
                    site_name = request.session.get('company_name')
                    c = {
                        "email": user.email,
                        'domain': request.get_host(),
                        'site_name': site_name,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
            return redirect(urls_paths['password_reset_done']['redirect'])
    else:
        form = CustomPasswordResetForm()

    context = {
        'urls_paths': urls_paths,
        'form': form,
        'return_to_previous_page': return_to_previous_page,
    }
    return render(request, urls_paths['password_reset_email']['render'], context)
