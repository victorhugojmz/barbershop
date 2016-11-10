from django.conf.urls import include , url
from . import views
app_name= 'cita'
urlpatterns = [
    #/music/ homepage
    url(r'^$', views.index , name='index'), #index for each individual apply 
    url(r'book/$', views.book , name='book'), 
]

 