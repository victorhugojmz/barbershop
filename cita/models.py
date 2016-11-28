from __future__ import unicode_literals
from django.db import models
import datetime 
class Cita(models.Model):
    hour_choices = (
        ('11:15','11 y cuarto'),
        ('11:40','11:45'),
        ('12:15','12:15'),
        ('12:30','12:30'),
    )
    cita_id = models.AutoField(
                        primary_key= True
                        )
    fecha_cita = models.DateField(
                        'Fecha'
                        )
    fecha_creacion_cita = models.DateTimeField(
                        auto_now=False,
                        auto_now_add= True,
                        blank=True, 
                        null=True 
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
                        null=False,
                        choices = hour_choices
                        )