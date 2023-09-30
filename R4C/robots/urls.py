from django.urls import path

from .views import create_robots_api


urlpatterns = [
    path('api/robo-create/', create_robots_api, name='CreateRobotsAPI'),
]
