from django.urls import path, include
from rest_framework import routers
from .views import AppointmentViewSet, create_appointment, my_appointments

router = routers.DefaultRouter()
router.register(r'appointment', AppointmentViewSet)


urlpatterns = [
    path('appointment/create/', create_appointment, name='create_appointment'),
    path('appointment/my/', my_appointments, name='my_appointments'),
    path('', include(router.urls))
]

