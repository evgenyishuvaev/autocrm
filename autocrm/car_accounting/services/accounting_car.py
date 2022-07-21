from django.http import HttpRequest

from ..models import Car, Model
from ..forms import AddCar, StatisticsForm


def validate_and_save_add_form(request: HttpRequest):
    """
    Заполняем все скрытые поля и возвращаем форму для дальнейшеей валидации и сохранения в бд
    """

    # используется для запроса автомобиля в бд
    filtered_field = request.POST.copy()
    filtered_field.pop("csrfmiddlewaretoken")
    car = Car.objects.filter(**filtered_field.dict())

    # если уже есть машина с таким гос номером, моделью и годом выпуска, тогда это повторный учет, иначе нет
    is_re_registration = True if car else False

    mark = Model.objects.all().filter(model=request.POST['model'])[0].mark_id

    form_fields = request.POST.copy()
    form_fields.setdefault('mark', mark)
    form_fields.setdefault('owner', request.user.username)
    form_fields.setdefault('re_registration', is_re_registration)

    form = AddCar(form_fields)
    return form


def get_cars_from_db():
    """
    Достаем все записи автомобилей из бд
    """
    cars = Car.objects.all()
    context = {'cars': cars, 'title': 'List_of_cars'}
    return context


def get_filtered_rows_from_db(request):

    """
    Валидируем данные формы, затем обращаемся к бд за необходимыми записями.
    re_registration - определяет будут ли влючены записи с повторными учетами авто,
    по данным из формы достаем необходимые записи и возвращаем словаь context c этими данными
    """

    form = StatisticsForm(request.POST)
    if form.is_valid():
        # кладем в словарь все не пустые значения из формы, будем использовать для запросов к бд
        fields_for_filter = {key: value for key, value in form.cleaned_data.items() if value}
        re_registration = fields_for_filter.get('re_registration')
        if re_registration:
            # все записи, включая повторные учеты
            fields_for_filter.pop('re_registration')
            result = Car.objects.filter(**fields_for_filter).values()
        else:
            # все записи, исключая повторные учеты
            result = Car.objects.filter(**fields_for_filter).exclude(re_registration=True).values()

        count_row = len(result)
        context = {'title': 'Statistics', 'result': result, 'count': count_row, 'form': form}

        return context
