from ..models import Car
from ..exceptions import UnavailableQueryParams


def validate_query_params(fields: list, query_params: dict):

    fields_for_exception = []

    for key in query_params:
        if key not in fields:
            fields_for_exception.append(key)

    if fields_for_exception:
        raise UnavailableQueryParams



def filtered_cars(request):
    """
    Берем из БД нужные данные, фильтруя по заполенным полям
    """
    fields = ["reg_num", "mark", "model", "release_year", "owner", "re_registration"]

    fields_for_filter = request.query_params.dict()
    validate_query_params(fields, fields_for_filter)
    re_registration = fields_for_filter.get("re_registration") # флаг для обозначния, включать повторный учет в выборку или нет
    if re_registration:
        fields_for_filter.pop("re_registration")
        return Car.objects.filter(**fields_for_filter)
    else:
        return Car.objects.filter(**fields_for_filter).exclude(re_registration=True)