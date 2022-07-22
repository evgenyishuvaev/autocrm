from rest_framework.exceptions import APIException


class UnavailableQueryParams(APIException):
    status_code = 400
    default_detail = "Requested invalid query params"
    default_code = "Invalid query params"
