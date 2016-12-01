from __future__ import unicode_literals

from django.db import models
from productos.models import Producto
from index.models import Servicio
# Create your models here.
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField('Creacion',auto_now_add=True,blank=False)
    total_venta = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.fecha_venta