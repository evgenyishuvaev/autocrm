from django.urls import path
from .views import add_car_form, get_cars

urlpatterns = [
    path('', get_cars, name='list_of_cars'),
    path('add_car', add_car_form, name='add_car')
]