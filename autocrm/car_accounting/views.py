from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest



from .services.accounting_car import validate_and_save_add_form, get_cars_from_db, get_filtered_rows_from_db
from .forms import AddCar, StatisticsForm



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

