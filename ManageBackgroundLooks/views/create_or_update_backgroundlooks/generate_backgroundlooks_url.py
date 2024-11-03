# ManageBackgroundLooks/views/create_or_update_backgroundlooks/generate_backgroundlooks_url.py
from django.urls import reverse

from ManageBackgroundLooks.models import MyBackgroundLooks


def generate_backgroundlooks_url(user):
    try:
        backgroundlook_obj = MyBackgroundLooks.objects.get(user=user)
        url = reverse('create_or_update_backgroundlooks',
                      kwargs={'user_id': user.pk, 'backgroundlooks_id': backgroundlook_obj.pk})
    except MyBackgroundLooks.DoesNotExist:
        url = reverse('create_or_update_backgroundlooks_no_id', kwargs={'user_id': user.pk})
    return url
