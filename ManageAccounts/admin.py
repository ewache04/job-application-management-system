# ManageAccounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ManageAccounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


# Register CustomUser with CustomUserAdmin
def reg_to_admin(model, admin_class):
    return admin.site.register(model, admin_class)


# Register CustomUser with CustomUserAdmin
reg_to_admin(CustomUser, CustomUserAdmin)
