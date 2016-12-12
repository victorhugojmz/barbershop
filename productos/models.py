from __future__ import unicode_literals
from django.db import models
from index.models import Barbero
# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(
                                primary_key= True
                                )
    nombre_producto = models.CharField(
                                max_length = 150
                                )
    tipo_producto = models.CharField(
                                max_length = 50
                                )
    marca_producto =  models.CharField(
                                max_length = 50
                                )
    precio_unitario_producto = models.DecimalField(
                                max_digits=6, 
                                decimal_places=2
                                )
    stock_producto = models.PositiveIntegerField()
    descripcion_producto = models.TextField()
    imagen_producto = models.FileField()
    def get_absolute_url(self):
        return reverse('index:detail', kwargs={'pk': self.pk })
    def __str__(self):
        return self.nombre_producto
class Salida(models.Model):
    barbero = models.ForeignKey(Barbero)
    id_producto = models.IntegerField()
    cantidad = models.IntegerField(
                default=0, 
                blank=False, 
                null=False
                )
    concepto = models.CharField(
                max_length=10, 
                blank=False, 
                null=False
                )
    fecha_operacion  = models.DateTimeField( 
                        auto_now=False,
                        auto_now_add= True,
                        blank=True, 
                        null=True 
                        )
class Proveedor(models.Model):
    nombre = models.CharField(
                        max_length = 70,
                        blank= False,
                         null=True)
    telefono = models.CharField(
        max_length= 15
        )
    email = models.CharField(
        max_length =20
        )
    def __str__(self):
            return  self.nombre
class Entrada(models.Model):
    id_producto = models.IntegerField(
                        default = 0,
                        blank=False,
                        null=False
                        )  
    cantidad = models.IntegerField(
                        default = 0,
                        blank=False,
                        null=False
                        )
    producto = models.ForeignKey(Producto)
    fecha_operacion = models.DateTimeField(
                        auto_now=False,
                        auto_now_add= True,
                        blank=True, 
                        null=True 
                        )                                  
    proveedor = models.ForeignKey(Proveedor)