from __future__ import unicode_literals
from django.db import models
class Galeria(models.Model):
    id_imagen = models.AutoField(primary_key= True)
    descripcion = models.CharField(
                    max_length = 200,
                    blank=True, 
                    null=True
                    )
    titulo_imagen = models.CharField(
                    max_length = 100,
                    blank=True, 
                    null=True
                    ) 
    imagen  = models.FileField(
                    blank=False, 
                    null=False
                    )
    def get_absolute_url(self):
        return reverse('index:gallery-details', kwargs={'pk': self.pk })
class Barbero(models.Model):
    id_barbero = models.AutoField(primary_key=True)
    nombre_barbero  = models.CharField(
                        max_length = 60
                        )
    cuenta_twitter_barbero = models.CharField(
                        max_length = 30,
                        blank=True, 
                        null=True
                        )
    cuenta_facebook_barbero = models.CharField(
                        max_length = 30,
                        blank=True, 
                        null=True
                        )
    descripcion_barbero =  models.TextField(
                        max_length = 350
                        )
    fotografia_barbero = models.FileField()
    def __unicode__(self):
            return  self.nombre_barbero  + '\n' + self.cuenta_twitter_barbero + '\n' + self.cuenta_facebook_barbero + '\n' + self.descripcion_barbero     
class Servicio(models.Model): 
    nombre_servicio  = models.CharField(
                        max_length = 30,
                        default="Corte de pelo"
                        )
    tipo_servicio   = models.CharField(
                        max_length = 50
                        )
    imagen_corte = models.CharField(
                        max_length = 200)
    precio_servicio =  models.IntegerField()
    def __unicode__ (self):
        return self.nombre_corte + '-' + self.descripcion_corte  + '-' + self.imagen_corte