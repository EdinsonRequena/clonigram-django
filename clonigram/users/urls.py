"""Users URLs.
"""
# Django Modules.
from django.urls import path
# Users Modules.
from users import views

urlpatterns = [

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Managment
    path(
        route='login/',
        view=views.login_view,
        name='login'
        ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup, name='signup'
        ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update'
    ),
]
