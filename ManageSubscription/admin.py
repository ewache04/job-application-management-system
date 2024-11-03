# ManageSubscription/admin.py
from django.contrib import admin

from ManageSubscription.models import UserPayment


class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_bool', 'stripe_checkout_id', 'subscription_active', 'refund_requested',)
    search_fields = ('user__username', 'stripe_checkout_id', 'subscription_active', 'refund_requested')


# Function to register a model with the admin site
def register_model_with_admin(model, admin_class):
    admin_site = admin.site
    try:
        admin_site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        admin_site.unregister(model)
        admin_site.register(model, admin_class)


# Register models with the admin site
register_model_with_admin(UserPayment, UserPaymentAdmin)
