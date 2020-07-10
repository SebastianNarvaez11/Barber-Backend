from django.shortcuts import render
from django.http import HttpResponse, Http404
from modules.users.models import User
from rest_framework import viewsets
from rest_framework import permissions
from modules.base.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from modules.base.serializers import CustomTokenObtainPairSerializer

def index(request):
    return render(request, "index.html")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer