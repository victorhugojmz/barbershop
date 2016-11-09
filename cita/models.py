from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Producto(models.Model):
    tipo = models.CharField(max_length = 120)
    precio  =  models.IntegerField()
    stock = models.IntegerField()
    descripcion  = models.CharField(max_length = 250)
class Cita(models.Model):
    cita_id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length = 150)
    fecha = models.DateField()
