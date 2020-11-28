from django.urls import re_path, include

from .views import RegistrationAPIView
from .views import LoginAPIView

urlpatterns = [
    re_path("registration/", RegistrationAPIView.as_view(), name='user_registration'),
    re_path("login/", LoginAPIView.as_view(), name='user_login'),
]