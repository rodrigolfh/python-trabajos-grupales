from django.db import models
from django.contrib.auth.models import User #<-- esto se agregó manualmente
import datetime

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    fecha_nacimiento = models.DateField()
    genero = models.CharField(
        max_length=6,
        choices = [('m', 'f'),('f', 'm'),('o','o')]
    )
    #vincularlos ondelete tb para evitar informacion huerfana
    #esto es eauivalente a 1:1 foreign key, lo usaremos para vinclar
    #una instancia de objeto user con una instancia de "Account"

    def __str__(self):
        return self.user.username
    #esto de acá servirá para poder referenciar el uusario cno más facilidad.

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=50, unique=True) 
    rut_empresa = models.CharField(max_length=13, unique=True)
    contacto = models.CharField(max_length=50)
    email_contacto = models.EmailField(verbose_name="Mail de contacto", unique=True)
    telefono_contacto = models.CharField(max_length=15, default="")
    fecha_inscripcion = models.DateField(datetime.date.today())
    
    def __str__(self):
        return self.razon_social