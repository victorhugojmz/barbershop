from __future__ import unicode_literals
from django.db import models
class Cita(models.Model):
    cita_id = models.AutoField(primary_key= True)
    fecha_cita = models.DateTimeField()
    fecha_creacion_cita = models.DateField('Creacion', auto_now= True , blank=True)
    nombre_cliente = models.CharField(max_length = 150)
    telefono_cliente =  models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 120)
