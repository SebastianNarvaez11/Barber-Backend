from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from modules.products.models import Product
from modules.users.models import User
from modules.appointments.models import Appointment
from django.db.models import Count, F, Value, Sum
from django.db.models.functions import Concat
from django.db.models.functions import TruncMonth
from django.utils import timezone

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def get_report(request):
    try:
        report = request.POST.get("report")
        data = []
        if report == 'top-services':
            data = Product.objects.all().annotate(count=Count('appointment__id')).values('id','name', 'count').order_by('-count')
        elif report == 'top-clients':
            data = User.objects.filter(role="CLIENTE").annotate(count=Count('appointment__id'), name=Concat('first_name',Value(' '), 'last_name')).values('id','name', 'count').order_by('-count')
        elif report == 'appointments-by-month':
            current_year = timezone.now().year
            data = Appointment.objects.filter(status='REALIZADA', end_date__year=current_year).exclude(end_date=None).annotate(month=TruncMonth('end_date')).values('month').annotate(count=Count('id')).values('month', 'count')
        elif report == 'sales-by-month':
            current_year = timezone.now().year
            data = Appointment.objects.filter(status='REALIZADA', end_date__year=current_year).exclude(end_date=None).annotate(month=TruncMonth('end_date')).values('month').annotate(value=Sum('final_price')).values('month', 'value')
        return Response(data)
    except:
        return Response(["Ocurrió un error, intente nuevamente"], status=500)
    