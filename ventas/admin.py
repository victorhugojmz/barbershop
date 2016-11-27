from django.contrib import admin
from .models import Venta , VentaProducto
# Register your models here.
class VentasModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Venta
        list_display = ('id_venta','fecha_venta','total_venta')
        list_filter = ('fecha_venta')
admin.site.register(VentaProducto)