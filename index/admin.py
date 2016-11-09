from django.contrib import admin
from .models import Producto, Barbero , Servicio , Galeria
# Register your models here.
admin.site.register(Barbero)
admin.site.register(Servicio)
admin.site.register(Galeria)
admin.site.register(Producto)
