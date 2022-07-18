from django.urls import path, include

from rest_framework import routers

from .views import add_car, get_cars, get_statistics, CarApiView
from .api_schemas import urlpatterns as doc_url


router = routers.DefaultRouter()
router.register(r'cars', CarApiView, basename='cars')


urlpatterns = [
    path('', get_cars, name='list_of_cars'),
    path('add_car', add_car, name='add_car'),
    path('statistics', get_statistics, name='statistics'),

    # --------------REST-------------------
    path('api/v1/', include(router.urls))
]

urlpatterns += doc_url