from __future__ import unicode_literals

from django.db import models
class Cita(models.Model):
    cita_id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length = 150)
    fecha = models.DateField()