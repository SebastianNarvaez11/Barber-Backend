from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, ProductoPhotoViewSet, list_products

router = routers.DefaultRouter()
router.register(r'product', ProductoViewSet)
router.register(r'product_photo', ProductoPhotoViewSet)



urlpatterns = [
    path('product/list/', list_products, name='list_products'),
    path('', include(router.urls))
]

