from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AppointmentSerializer
from .models import Appointment
from modules.users.models import User
import datetime
from django.utils import timezone
import json
import random
from django.db.models import Q
# Create your views here.


class AppointmentViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def filter_queryset(self, queryset):
        queryset = super(AppointmentViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-date')

@api_view(['POST'])
def create_appointment(request):
    try:
        email = request.POST.get("email")
        products = request.POST.get("products")
        products = json.loads(products)
        if not email or not products or len(products) == 0:
            raise

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        telephone = request.POST.get("telephone")
        notes = request.POST.get("notes")
        start_date = request.POST.get("start_date")
        estimated_price = request.POST.get("estimated_price")

        user_client, created = User.objects.get_or_create(username=email)
        user_client.email = email
        user_client.telephone = telephone
        if created:
            user_client.first_name = first_name
            user_client.last_name = last_name
            user_client.set_password("Demo1234")
        user_client.save()

        python_date = datetime.datetime.fromtimestamp(int(start_date), tz=timezone.utc)
        appointment, created_appointment = Appointment.objects.get_or_create(user=user_client, status="PENDIENTE", date=python_date)
        appointment.notes = notes
        appointment.estimated_price = estimated_price
        appointment.product.clear()
        for product in products:
            appointment.product.add(product)
        appointment.owner = user_client
        
        users = User.objects.filter(role='PELUQUERO', is_active=True)
        appointment.barber = random.choice(users)

        appointment.save(request=request)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    except:
        return Response(["Ocurrió un error, intente nuevamente"], status=500)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def my_appointments(request):
    products = Appointment.objects.filter(
        Q(
           Q(user = request.user) | Q(barber = request.user) | Q(owner = request.user)
        )
    ).exclude(user=None).order_by('status', '-date')
    serializer = AppointmentSerializer(products, many=True)
    return Response(serializer.data)
