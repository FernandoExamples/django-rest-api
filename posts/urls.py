from django.urls import path
from .api.views import PostViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view()),
]
