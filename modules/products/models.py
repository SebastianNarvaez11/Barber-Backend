from django.db import models
from modules.base.models import Base

class Product(Base):
    STATUS_TYPE_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),]

    name = models.CharField(blank=True, null=True, verbose_name="Nombre", max_length=255)
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.FloatField(blank=True, null=True, max_length=100, verbose_name="Precio")
    duration = models.FloatField(blank=True, null=True, max_length=20, verbose_name="Duración en minutos")
    status = models.CharField(verbose_name='Estado', max_length=20, choices=STATUS_TYPE_CHOICES, default='ACTIVO') 

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        

class ProductPhoto(Base):
    product = models.ForeignKey('Product', related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads', null=True, blank=True)

    def handle_uploaded_file(self, file):
        from django.conf import settings
        import os

        file_path = os.path.join(settings.UPLOADS_ROOT, self.id)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)