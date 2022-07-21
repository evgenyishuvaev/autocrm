from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser

from .services.rest_api import filtered_cars
from .serializers import CarSerializer


class CarApiView(ReadOnlyModelViewSet):
    """
    Представления REST API  - '/cars' и '/cars/<int:pk>'
    """
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        return filtered_cars(self.request)

def get_swagger(request):
    return render(request, template_name='car_accounting/swagger_ui.html')