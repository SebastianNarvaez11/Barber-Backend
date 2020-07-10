from django.urls import path, include
from rest_framework import routers
from .views import get_report

urlpatterns = [
    path('reports/', get_report, name='get_report'),
]

