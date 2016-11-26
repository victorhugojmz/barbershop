from django.conf.urls import include ,url
from . import views
app_name = 'index'
urlpatterns = [
    url(r'^$', views.index , name='zamacueca'),
    url(r'^nosotros/$', views.about, name='about'),
    url(r'^galeria/$',  views.Galeria.as_view(), name='gallery'),
    url(r'^galeria/nueva/$',  views.NuevaImagen.as_view(), name='gallery-create'),
    url(r'^galeria/(?P<pk>[0-9]+)/eliminar/$',  views.EliminaImagen.as_view(), name='gallery-delete'),
    url(r'^galeria/(?P<pk>[0-9]+)/$',  views.DetallesImagen.as_view(), name='gallery-details'),
] 