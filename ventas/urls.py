from django.conf.urls import include , url
from . import views
app_name = 'productos'
urlpatterns  = [
    url(r'^$', views.index_citas , name='index'),
]