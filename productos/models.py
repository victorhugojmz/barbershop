from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key= True)
    nombre_producto = models.CharField(max_length = 150)
    tipo_producto = models.CharField(max_length = 50)
    marca_producto =  models.CharField(max_length = 50)
    precio_unitario_producto = models.IntegerField(default= 0)
    stock_producto = models.IntegerField(default=0)
    descripcion_producto = models.TextField()
    def get_absolute_url(self):
        return reverse('index:detail', kwargs={'pk': self.pk })
class Imagen(models.Model):
    titulo_imagen = models.ForeignKey(Producto , on_delete=models.CASCADE) 
    imagen = models.FileField()
    descripcion_imagen  = models.CharField(max_length = 80)
    