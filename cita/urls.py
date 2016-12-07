from django.conf.urls import include , url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
from . import views
app_name= 'cita'
urlpatterns = [
    #/urls para cita app
    url(r'^$', login_required(views.index) , name='index'), #index for each individual apply
    url(r'all/$',login_required(views.all_citas), name='all-citas'),
    url(r'nueva/$', views.book , name='book'),
    url(r'editar/(?P<pk>[0-9]+)/$', login_required(views.UpdateCitaView.as_view()), name='update-cita'),
    url(r'eliminar/(?P<pk>[0-9]+)/$', login_required(views.DeleteCita.as_view()), name='delete-cita'),
    #API 
    url(r'api/citas/$', views.ListaDeCitas.as_view(),name='get-citas'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
