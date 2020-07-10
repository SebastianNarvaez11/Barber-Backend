from rest_framework import serializers
from .models import Product, ProductPhoto


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'product', 'photo', 'deleted']
        extra_kwargs = {'photo': {'required': False}}


class ProductSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'duration', 'status', 'deleted', 'photos']
