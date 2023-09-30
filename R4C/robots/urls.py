from django.urls import path

from .views import create_robots_api, download_weekly_excel


urlpatterns = [
    path('api/robo-create/', create_robots_api, name='CreateRobotsAPI'),
    path('excel-download/', download_weekly_excel, name='DownloadWeeklyXL'),
]
