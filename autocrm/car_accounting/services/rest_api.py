from ..models import Car


def filtered_cars(request):
    """
    Берем из БД нужные данные, фильтруя по заполенным полям
    """
    fields_for_filter = request.query_params.dict()
    re_registration = fields_for_filter.get("re_registration") # флаг для обозначния, включать повторный учет в выборку или нет
    if re_registration:
        fields_for_filter.pop("re_registration")
        return Car.objects.filter(**fields_for_filter)
    else:
        return Car.objects.filter(**fields_for_filter).exclude(re_registration=True)