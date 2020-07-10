from django.contrib.auth.models import UserManager, AbstractBaseUser
from modules.base.models import Base
from django.db import models
import hashlib, random

class User(AbstractBaseUser):
    USER_TYPE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('CLIENTE', 'Cliente'),
        ('PELUQUERO', 'Peluquero'),]

    id = models.CharField(primary_key=True, blank=True, max_length=40, verbose_name="ID")
    username = models.CharField(max_length=100, unique=True, verbose_name="Nombre de usuario")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    first_name = models.CharField(max_length=100, default='', verbose_name="Nombre")
    last_name = models.CharField(max_length=100, default='', verbose_name="Apellidos")
    role = models.CharField(verbose_name='Rol', max_length=10, choices=USER_TYPE_CHOICES, default='CLIENTE') 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    telephone = models.CharField(max_length=100, blank=True, null=True,verbose_name="Teléfono")

    USERNAME_FIELD = 'username'
    objects = UserManager()


    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-date_joined']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, use_events=True, request=None):
        is_new = False
        if not self.id:
            from django.core import signing
            self.id = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()
            is_new = True

        super(User, self).save(force_insert, force_update, using, update_fields)