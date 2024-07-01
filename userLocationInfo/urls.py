from django.urls import path
from .views import get_user_info

urlpatterns = [
    path('hello', get_user_info)
]
