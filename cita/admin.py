from django.contrib import admin
from .models import Cita
class CitasModelAdmin(admin.ModelAdmin):
    list_display = ['cita_id','fecha_creacion_cita','fecha_cita','nombre_cliente','telefono_cliente']
    list_filter = ['fecha_creacion_cita','fecha_cita']
    class Meta:
        model = Cita
admin.site.register(Cita,CitasModelAdmin)