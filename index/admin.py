from django.contrib import admin
from .models import Producto, Barbero , Servicio , Imagen
# Register your models here.
admin.site.register(Barbero)
admin.site.register(Servicio)
admin.site.register(Imagen)
admin.site.register(Producto)