from django.conf.urls import include , url
from . import views
app_name = 'productos'
urlpatterns  = [
    url(r'^$',, name='index'),
]