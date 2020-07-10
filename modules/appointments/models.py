from django.db import models
from modules.base.models import Base

class Appointment(Base):
    STATUS_TYPE_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN PROCESO', 'En proceso'),
        ('RECHAZADA', 'Rechazada'),
        ('REALIZADA', 'Realizada'),]
    product = models.ManyToManyField('products.Product', blank=True, verbose_name="Servicio")
    date = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de la cita")
    user = models.ForeignKey('users.User', blank=True, null=True, verbose_name="Usuario", on_delete=models.CASCADE)
    notes = models.TextField(verbose_name="Notas", blank=True, null=True)
    estimated_price = models.FloatField(blank=True, null=True, verbose_name="Precio estimado")
    estimated_discount = models.FloatField(blank=True, null=True, verbose_name="Descuento estimado (valor)")
    estimated_discount_rate = models.FloatField(blank=True, null=True, verbose_name="Descuento estimado (tasa)")
    estimated_duration = models.FloatField(blank=True, null=True, max_length=20, verbose_name="Duración estimada en minutos")
    final_price = models.FloatField(blank=True, null=True, verbose_name="Precio final")
    final_discount = models.FloatField(blank=True, null=True, verbose_name="Descuento final (valor)")
    final_discount_rate = models.FloatField(blank=True, null=True, verbose_name="Descuento final (tasa)")
    final_duration = models.FloatField(blank=True, null=True, max_length=20, verbose_name="Duración final en minutos")
    rating = models.CharField(blank=True, null=True, max_length=20, verbose_name="Calificación")
    start_date = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de inicio")
    end_date = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de finalización")
    status = models.CharField(blank=True, null=True, max_length=100, verbose_name="Estado",  choices=STATUS_TYPE_CHOICES, default='PENDIENTE')
    barber = models.ForeignKey('users.User', blank=True, null=True, verbose_name="Peluquero/Barbero", on_delete=models.CASCADE, related_name="barbero")