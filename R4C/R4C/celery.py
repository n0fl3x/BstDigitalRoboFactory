import os

from celery import Celery
from django.conf import settings


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'R4C.settings',
    )

app = Celery(
    'R4C',
    broker='redis://localhost',
)

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY',
    )

app.autodiscover_tasks()
