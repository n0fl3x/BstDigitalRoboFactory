from json import JSONDecodeError, loads
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from .orm_functions import create_robot
from .validators import validate_json, validate_datetime_field


@csrf_exempt
def create_robots_api(request):
    """Функциональное вью для API-endpoint'а, принимающий JSON-объект POST-методом
    с информацией о созданных роботах с последующей их валидацией и сохранением в базу данных."""

    if request.method == 'POST':
        try:
            data = loads(request.body)
        # если прилетел кривой JSON
        except JSONDecodeError as er:
            return HttpResponseBadRequest(
                f'Cannot decode JSON: {er}',
                status=400,
            )

        # если в JSON'е один робот
        if type(data) == dict:
            if validate_json(json_data=data) and validate_datetime_field(datetime_text=data['created']):
                create_robot(info=data)
                return HttpResponse(
                    'New object was successfully added to database.',
                    status=201,
                )
            else:
                return HttpResponseBadRequest(
                    'JSON object is invalid.',
                    status=400,
                )

        # если >1 робота
        if type(data) == list:
            valid_objs = 0
            invalid_objs = 0

            for item in data:
                if validate_json(json_data=item) and validate_datetime_field(datetime_text=item['created']):
                    create_robot(info=item)
                    valid_objs += 1
                else:
                    # просто выведем на странице кол-во невалидных объектов
                    # вдруг какие-то другие нормальные и смогут сохраниться в БД
                    invalid_objs += 1

            return HttpResponse(
                f'{valid_objs} valid objects added to database.\n'
                f'{invalid_objs} invalid objects ignored.',
                status=201,
            )

    else:
        return HttpResponseBadRequest(
            'You need to pass your JSON data via POST-method.',
            status=405,
        )
