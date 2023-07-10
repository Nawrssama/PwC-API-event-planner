from django.urls import path
from .views import EventList, WeatherList, FlightList

urlpatterns = [
    path('events/', EventList.as_view(), name= 'events_list'),
    path('weather/', WeatherList.as_view(), name='weather_detail'),
    path('flights/', FlightList.as_view(), name='flight_detail'),
]