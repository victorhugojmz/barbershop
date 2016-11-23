from django.conf.urls import include ,url
from . import views
app_name = 'productos'
urlpatterns  = [
    url(r'^$', views.IndexView, name='index'),
    url(r'producto/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'nuevo/$' , views.ProductCreate.as_view( ), name="product-add"), 
    url(r'producto/actualizar/(?P<pk>[0-9]+)/$' , views.ProductUpdate.as_view( ), name="product-update"), 
    url(r'producto/(?P<pk>[0-9]+)/eliminar/$' , views.ProductDelete.as_view( ), name="product-delete"),
]