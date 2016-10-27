from django.conf.urls import include ,url
from . import views
app_name = 'encargado'
urlpatterns = [
        url(r'^$', views.encargado ,  name='index'),    
        url(r'register/$', views.UserFormView.as_view() , name='register'), 
        url(r'producto/',views.ProductsListView.as_view() ,name='productos'),       
]
