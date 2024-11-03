from django.contrib import admin

from ManageBackgroundLooks.models import MyBackgroundLooks


# Register your background image here.
class MyBackgroundLooksAdmin(admin.ModelAdmin):
    list_display = ('selected_background', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'selected_background')
    date_hierarchy = 'created_at'


# Function to register background image with admin site
def register_model_with_admin(model, admin_class):
    return admin.site.register(model, admin_class)


# Register background image model with admin site
register_model_with_admin(MyBackgroundLooks, MyBackgroundLooksAdmin)
