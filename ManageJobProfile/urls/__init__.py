# ManageJobProfile/urls/__init__.py
"""
ManageJobProfile URL Configuration

This module initializes the URL patterns for the ManageJobProfile app.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

# Import the function to initialize URL patterns
from ManageJobProfile.urls.urls import initialize_urlpatterns

# Call the function to get the urlpatterns
urlpatterns = initialize_urlpatterns()

