from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length = 150)
    tipo_producto = models.CharField(max_length = 50)
    marca_producto =  models.CharField(max_length = 50)
    precio_unitario_producto = models.IntegerField(default= 0)
    stock_producto = models.IntegerField(default=0)
    imagen_producto = models.CharField(max_length = 300)
#class kitProducto(models.Model):
    