from django.conf.urls import include ,url
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'productos'
urlpatterns  = [
    url(r'^$', views.IndexView, name='index'),
    url(r'salidas/historial/$', login_required(views.SalidasView),name='index-salidas'),
    url(r'entradas/historial/$',login_required(views.EntradasView),name='index-entradas'),
    url(r'producto/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'nuevo/$', login_required(views.ProductCreate.as_view()), name="product-add"), 
    url(r'producto/actualizar/(?P<pk>[0-9]+)/$' , login_required(views.ProductUpdate.as_view()), name="product-update"), 
    url(r'producto/(?P<pk>[0-9]+)/eliminar/$' , login_required(views.ProductDelete.as_view()), name="product-delete"),
]