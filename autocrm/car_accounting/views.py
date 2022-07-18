from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser

from .services.accounting_car import validate_and_save_add_form, get_cars_from_db, get_filtered_rows_from_db
from .models import Car
from .forms import AddCar, StatisticsForm
from .serializers import CarSerializer


@login_required
def add_car(request: HttpRequest):
    """
    Представление url /add_car
    """

    if request.method == "POST":
        form = validate_and_save_add_form(request)
        if form.is_valid():
            form.save()
            return redirect('list_of_cars')
    else:
        form = AddCar()

    return render(request, template_name='car_accounting/add_car.html', context={'form': form, 'title': 'Add car'})


@login_required
def get_cars(request: HttpRequest):
    """
    Представление url '/'
    """
    context = get_cars_from_db()
    return render(request, template_name='car_accounting/list_of_car.html', context=context)


@login_required
def get_statistics(request: HttpRequest):
    """
    Представление url '/statistics'
    """

    if request.method == 'POST':
        context = get_filtered_rows_from_db(request)
        return render(request, template_name='car_accounting/statistics.html', context=context)
    else:
        form = StatisticsForm()
        return render(request,
                      template_name='car_accounting/statistics.html',
                      context={'title': 'Statistics', 'form': form}
                      )


# ----------------REST----------------

class CarApiView(ReadOnlyModelViewSet):

    serializer_class = CarSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        fields_for_filter = self.request.query_params.dict()
        re_registration = fields_for_filter.get("re_registration")
        print(fields_for_filter)
        if re_registration:
            fields_for_filter.pop("re_registration")
            return Car.objects.filter(**fields_for_filter)
        else:
            return Car.objects.filter(**fields_for_filter).exclude(re_registration=True)


def get_swagger(request):
    return render(request, template_name='car_accounting/swagger_ui.html')
