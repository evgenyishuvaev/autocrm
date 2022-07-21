from django.urls import path, include

from rest_framework import routers

from .views import add_car, get_cars, get_statistics
from .api_views import  CarApiView, get_swagger



urlpatterns = [
    path('', get_cars, name='list_of_cars'),
    path('add_car', add_car, name='add_car'),
    path('statistics', get_statistics, name='statistics'),


]
