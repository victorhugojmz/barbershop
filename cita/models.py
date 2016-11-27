from __future__ import unicode_literals
from django.db import models
import datetime 
class Cita(models.Model):
    cita_id = models.AutoField(primary_key= True)
    fecha_cita = models.DateField(
                        blank=False, 
                        null=False
                        )
    fecha_creacion_cita = models.DateTimeField(
                        auto_now=False,
                        auto_now_add= True 
                        )
    nombre_cliente = models.CharField(
                        max_length = 150,
                        blank=False, 
                        null=False
                        )
    telefono_cliente =  models.CharField(
                        max_length = 20,
                        blank=False, 
                        null=False
                        )
    direccion = models.CharField(
                        max_length = 120,
                        blank=True, 
                        null=True
                        )
    hora_cita = models.TimeField(
                        'Hora',
                        blank=False, 
                        null=False
                        )