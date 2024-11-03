from django.contrib import admin
from .models import UserKey


# Register your open_model_group here.


class UserKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key_name', 'key_value', 'is_default', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'key_name')
    date_hierarchy = 'created_at'


# Function to register open_model_group with admin site
def register_model_with_admin(model, admin_class):
    return admin.site.register(model, admin_class)


# Register UserKey model with admin site
register_model_with_admin(UserKey, UserKeyAdmin)
