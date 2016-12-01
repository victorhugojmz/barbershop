from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length =200, db_index= True)
    slug = models.SlugField(max_length = 200, db_index=True , unique = True)
    class Meta:
        orden = ('nombre',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorías'
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,related_name='productos')
    nombre = models.CharField(max_length= 200, db_index= True)
    slug = models.SlugField(max_length= 200, db_index=True)
    image = models.FileField()
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    esta_disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    class Meta:
        orden = ('nombre',)
        index_together ('id','slug')
    def __str__(self):
        return self.name