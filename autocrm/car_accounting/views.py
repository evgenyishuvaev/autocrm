from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .models import Cars
from .forms import AddCar, StatisticsForm


@login_required
def add_car(request: HttpRequest):

    if request.method == "POST":
        form = AddCar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_cars')
    else:
        form = AddCar()

    return render(request,
                  template_name='car_accounting/add_car.html',
                  context={'form': form, 'title': 'Add car', 'username': request.user.username}
                  )


@login_required
def get_cars(request):
    cars = Cars.objects.all()
    return render(request,
                  template_name='car_accounting/list_of_car.html',
                  context={'cars': cars, 'title': 'List_of_cars'}
                  )


# @login_required
# def get_statistics(request):
#     form = StatisticsForm()
#
#     if request.method == 'POST':
#         form = StatisticsForm(request.POST)
#         if form.is_valid():
#             field_for_filter = request.POST.copy()
#             print(field_for_filter)
#             del field_for_filter['csrfmiddlewaretoken']
#             result = Cars.objects.all().filter(**field_for_filter)
#             return render(request,
#                           template_name='car_accounting/statistics.html',
#                           context={'title': 'Statistics', 'result': result, 'form': form}
#                           )
#
#     else:
#         return render(request,
#                       template_name='car_accounting/statistics.html',
#                       context={'title': 'Statistics', 'form': form}
#                       )
