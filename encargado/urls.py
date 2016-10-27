from django.conf.urls import include ,url
from . import views
app_name = 'encargado'
urlpatterns = [
        url(r'^$', views.encargado ,  name='index'),
]
