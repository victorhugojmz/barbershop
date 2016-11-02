from __future__ import unicode_literals
from django.db import models

class Barbero(models.Model):
    nombre_barbero  = models.CharField(max_length = 60)
    cuenta_twitter_barbero = models.CharField(max_length = 30)
    cuenta_facebook_barbero = models.CharField(max_length = 30)
    descripcion_barbero =  models.CharField(max_length = 350)
    
    def __unicode__(self):
            return  self.nombre_barbero  + '\n' + self.cuenta_twitter_barbero + '\n' + self.cuenta_facebook_barbero + '\n' + self.descripcion_barbero     
class Servicio(models.Model): 
    nombre_servicio  = models.CharField(max_length = 30,default="Corte de pelo")
    tipo_servicio   = models.CharField(max_length = 50)
    imagen_corte = models.CharField(max_length = 200)
    precio_servicio =  models.IntegerField()
    def __unicode__ (self):
        return self.nombre_corte + '-' + self.descripcion_corte  + '-' + self.imagen_corte
class Cita(models.Model): 
    nombre_cliente = models.CharField(max_length = 60)
    telefono_cliente = models.CharField(max_length = 20, default='044(55)29229929')
    direccion_cliente  = models.CharField(max_length = 150, default= 'Dr. Barragan No. 594')
    confirmacion = models.BooleanField(default= False)
    nombre_servicio = models.CharField(max_length = 60 , default="Corte de pelo")
class Imagen(models.Model):
    descripcion = models.CharField(max_length = 250)
    imagen  = models.FileField()