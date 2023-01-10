from django.urls import path
from .views import RegisterView, CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login', CustomAuthToken.as_view()),
    path('register', RegisterView.as_view())
]
