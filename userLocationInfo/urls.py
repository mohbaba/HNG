from django.urls import path
from .views import get_user_info, index

urlpatterns = [
    path('', index),
    path('api/hello', get_user_info)
]
