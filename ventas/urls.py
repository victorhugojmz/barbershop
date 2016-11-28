from django.conf.urls import include , url
from . import views
app_name = 'ventas'
urlpatterns  = [
    url(r'^$', views.index_citas , name='index'),
    url(r'nueva/$', views.genera_venta,name='sale-create'),   
]