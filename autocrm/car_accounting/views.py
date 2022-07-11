from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .models import Car, Model
from .forms import AddCar, StatisticsForm


@login_required
def add_car(request: HttpRequest):

    if request.method == "POST":
        mark = Model.objects.all().filter(model=request.POST['model'])[0].mark_id
        form_fields = request.POST.copy()
        form_fields.setdefault('mark', mark)
        form = AddCar(form_fields)
        print(form.fields)
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
def get_cars(request: HttpRequest):
    cars = Car.objects.all()
    return render(request,
                  template_name='car_accounting/list_of_car.html',
                  context={'cars': cars, 'title': 'List_of_cars'}
                  )


@login_required
def get_statistics(request: HttpRequest):
    form = StatisticsForm()

    if request.method == 'POST':
        form = StatisticsForm(request.POST)
        if form.is_valid():
            fields_for_filter = {key: value for key, value in form.cleaned_data.items() if value}

            result = Car.objects.all().filter(**fields_for_filter).values()
            count_row = len(result)
            print(result)
            return render(request,
                          template_name='car_accounting/statistics.html',
                          context={'title': 'Statistics',
                                   'result': result,
                                   'count': count_row,
                                   'form': form}
                          )

    else:
        return render(request,
                      template_name='car_accounting/statistics.html',
                      context={'title': 'Statistics', 'form': form}
                      )
