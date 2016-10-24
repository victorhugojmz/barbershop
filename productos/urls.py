from django.conf.urls import include, url
from . import views
app_name = 'productos'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^/create/$', views.DetailView.as_view(), name='create'),  
    url(r'^/delete/$', views.DetailView.as_view(), name='delete'),  
    url(r'^/update/$', views.DetailView.as_view(), name='uupdate'),        
]