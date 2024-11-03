# general_utils/configure_email_settings.py
import os

from general_utils.get_env_variable import get_env_variable


def configure_email_settings():
    if os.getenv('DJANGO_DEVELOPMENT') == 'True':
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    else:
        # Production email configuration
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = get_env_variable('EMAIL_HOST')
        EMAIL_PORT = int(get_env_variable('EMAIL_PORT'))
        EMAIL_USE_TLS = get_env_variable('EMAIL_USE_TLS') == 'True'
        EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')

    # Ensure you have a default "from" email address
    DEFAULT_FROM_EMAIL = 'webmaster@yourdomain.com'

    print("EMAIL_BACKEND:", EMAIL_BACKEND)
    if EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
        print(f"EMAIL_HOST: {EMAIL_HOST}")
        print(f"EMAIL_PORT: {EMAIL_PORT}")
        print(f"EMAIL_USE_TLS: {EMAIL_USE_TLS}")
        print(f"EMAIL_HOST_USER: {EMAIL_HOST_USER} ")
        print(f"EMAIL_HOST_PASSWORD: {EMAIL_HOST_PASSWORD}")

    return {
        'EMAIL_BACKEND': EMAIL_BACKEND,
        'EMAIL_HOST': EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend' and EMAIL_HOST or '',
        'EMAIL_PORT': EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend' and EMAIL_PORT or 0,
        'EMAIL_USE_TLS': EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend' and EMAIL_USE_TLS or False,
        'EMAIL_HOST_USER': EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend' and EMAIL_HOST_USER or '',
        'EMAIL_HOST_PASSWORD': EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend' and EMAIL_HOST_PASSWORD or '',
        'DEFAULT_FROM_EMAIL': DEFAULT_FROM_EMAIL,
    }
