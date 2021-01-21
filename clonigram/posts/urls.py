"""Posts URLs.
"""

#Django Modules.
from django.urls import path
# Posts Modules.
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed' # Localhost:8000
        ),
    path(
        route='posts/new',
        view=views.create_post,
        name='create'
    ),
]
