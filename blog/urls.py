from .views import (BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView)
from django.urls import path

urlpatterns = [
    path('posts/', BlogListCreateAPIView.as_view()),
    path('posts/<str:pk>', BlogRetrieveUpdateDestroyAPIView.as_view()),
]
