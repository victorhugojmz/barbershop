from __future__ import unicode_literals

from django.db import models
from productos.models import Producto
from index.models import Servicio, Barbero
# Create your models here.
class  Venta(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(
                            'Creacion',
                            auto_now_add=True,
                            blank=False
                        )
    total_venta = models.DecimalField(
                            max_digits=6, 
                            decimal_places=2,
                            blank=True, 
                            null=True)
    servicio = models.ForeignKey(Servicio)
    barbero = models.ForeignKey(Barbero) 