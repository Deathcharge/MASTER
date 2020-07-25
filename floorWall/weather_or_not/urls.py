from django.urls import path
from . import views

urlpatterns = [
   path("weather", views.index, name="weather_or_not"),
]