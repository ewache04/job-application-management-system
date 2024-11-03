# middleware/check_login_middleware.py

from django.shortcuts import redirect
from django.urls import reverse

from OpenColabAI.settings import urls_paths


class CheckLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is accessing a protected URL without authentication
        if not request.user.is_authenticated and request.path.startswith('/user/'):
            # Redirect to the login page with the next parameter to preserve intended redirection after login
            return redirect(reverse(urls_paths['login']['redirect']) + '?next=' + request.get_full_path())

        return response
