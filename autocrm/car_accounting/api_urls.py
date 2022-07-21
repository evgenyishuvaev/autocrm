from django.urls import path, include
from rest_framework import routers

from car_accounting.api_views import CarApiView, get_swagger


router = routers.DefaultRouter()
router.register(r'cars', CarApiView, basename='cars')


urlpatterns = [
    path('car_accounting/', include(router.urls)),
    path('swagger/', get_swagger, name='swagger_ui')
]


