"""peluqueria_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf.urls import url, include
from modules.base import views
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

api_urls = [
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('v1/', include('modules.users.urls')),#CRUD Users
    path('v1/', include('modules.products.urls')),#CRUD Products
    path('v1/', include('modules.appointments.urls')),#CRUD Products
    path('v1/', include('modules.reports.urls')),#CRUD Products
    re_path(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = [
    re_path('^api/', include(api_urls))]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += [ 
    re_path(r'^.*/', views.index),
    path('', views.index),
]