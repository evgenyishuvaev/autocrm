from django.shortcuts import render, redirect

from .models import Cars
from .forms import AddCar
# Create your views here.


def add_car_form(request):

    if request.method == "POST":
        form = AddCar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_cars')
    else:
        form = AddCar()
    return render(request, template_name='car_accounting/add_car.html', context={'form': form, 'title': 'Add car'})


def get_cars(request):
    cars = Cars.objects.all()
    return render(request,
                  template_name='car_accounting/list_of_car.html',
                  context={'cars': cars, 'title': 'List_of_cars'}
                  )
