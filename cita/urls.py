from django.conf.urls import include , url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
app_name= 'cita'
urlpatterns = [
    #/music/ homepage
    url(r'^$', views.index.as_view() , name='index'), #index for each individual apply 
    url(r'nueva/$', views.book , name='book'),
    url(r'api/citas/$', views.ListaDeCitas.as_view(),name='get-citas'),
    url(r'editar/(?P<pk>[0-9]+)/$', views.UpdateCitaView.as_view(), name='update-cita'),
    url(r'eliminar/(?P<pk>[0-9]+)/$', views.DeleteCita.as_view(), name='delete-cita'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

