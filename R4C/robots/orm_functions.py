from datetime import datetime
from django.db.models import Count
from django.db.models.query import QuerySet

from .models import Robot


def create_robot(info: dict) -> None:
    """ORM-запрос на создание экземпляра робота."""

    serial = info['model'] + "-" + info['version']
    model = info['model']
    version = info['version']
    created = info['created']

    Robot.objects.create(
        serial=serial,
        model=model,
        version=version,
        created=created,
    )


def get_unique_version_dicts(time_filter: datetime) -> QuerySet:
    """ORM-запрос для отбора queryset'а словарей с уникальными полями version
    и подсчётом количества произведённых экземпляров за указанный промежуток времени."""

    query_dicts = Robot.objects.filter(created__gte=time_filter).\
        values('model', 'version').\
        annotate(total=Count('model')).\
        order_by('total')

    return query_dicts
