from django.conf.urls import include , url
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'ventas'
urlpatterns  = [
    url(r'^$', login_required(views.index_citas) , name='index'),
    url(r'nueva/$', login_required(views.genera_venta),name='sale-create'),   
]