from django.urls import path,include
from .views import registration


app_name='users'

urlpatterns = [
    path("", registration, name='registration'),
]