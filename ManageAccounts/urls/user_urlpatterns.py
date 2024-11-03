# ManageAccounts/urls/user_urlpatterns.py
from django.urls import path


def get_user_urlpatterns():
    """
    Retrieve URL patterns for user-related views.

    This function defines URL patterns for user-related views, including user profile management,
    password reset, authentication, signup, and API endpoints.

    Returns:
        list: A list of URL patterns for user-related views.
    """
    # Import necessary modules
    from ManageAccounts.views.API.UserListCreate import UserListCreate
    from ManageAccounts.views.API.UserRetrieveUpdateDestroy import UserRetrieveUpdateDestroy
    from ManageAccounts.views.confirm_delete_user import confirm_delete_user
    from ManageAccounts.views.login_view import login_view
    from ManageAccounts.views.logout_view import logout_view
    from ManageAccounts.views.password.forgotten_password_recovery import password_reset_email, password_reset_done, \
        password_reset_confirm, password_reset_complete
    from ManageAccounts.views.password.update_password import update_password
    from ManageAccounts.views.payment_profile import payment_profile
    from ManageAccounts.views.signup import signup
    from ManageAccounts.views.update_profile import update_profile
    from ManageAccounts.views.user_account import user_account
    from ManageAccounts.views.user_details import user_details
    from ManageAccounts.views.user_home import user_home

    print("Initializing user URL patterns")

    user_urlpatterns = [
        # User home view for a specific user
        path('user/<int:user_id>/user_home/', user_home.home, name='user_home'),

        # User settings view for a specific user
        path('user/<int:user_id>/user_account/', user_account.user_account, name='user_account'),

        # User settings view for a payment profile
        path('user/<int:user_id>/payment_profile/<int:payment_id>/', payment_profile.payment_profile,
             name='payment_profile'),

        # User detail view for a specific user
        path('user/<int:user_id>/user_account/user_details/', user_details.user_details, name='user_details'),

        # Update profile view
        path('user/<int:user_id>/user_account/update_profile/', update_profile.update_profile, name='update_profile'),

        # Change password view
        path('user/<int:user_id>/user_account/change_password/', update_password.change_password,
             name='change_password'),

        # Reset password views
        path('password_reset/', password_reset_email.password_reset_email,
             name='password_reset_email'),
        path('password_reset/done/', password_reset_done.password_reset_done,
             name='password_reset_done'),
        path('reset/<uidb64>/<token>/', password_reset_confirm.password_reset_confirm,
             name='password_reset_confirm'),
        path('reset/done/', password_reset_complete.password_reset_complete,
             name='password_reset_complete'),

        # Confirm delete view
        path('user/<int:user_id>/user_account/confirm_delete_user/', confirm_delete_user.confirm_delete_user,
             name='confirm_delete_user'),



        # Signup view
        path('signup/', signup.signup, name='signup'),

        # Login view
        path('login/', login_view.login_view, name='login'),

        # Logout view
        path('logout/', logout_view.logout_view, name='logout'),

        # User List and Create API view
        path('users/', UserListCreate.UserListCreate.as_view(), name='user-list-create'),

        # User Retrieve, Update, and Destroy API view
        path('users/<int:pk>/', UserRetrieveUpdateDestroy.UserRetrieveUpdateDestroy.as_view(), name='user-detail-api'),

    ]

    print("Completed initializing user URL patterns")

    return user_urlpatterns
