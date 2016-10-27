from django.conf.urls import include ,url
from . import views
app_name = 'encargado'
urlpatterns = [
        url(r'^$', views.encargado ,  name='index'),    
        url(r'register/$', views.UserFormView.as_view() , name='register'), 
        url(r'producto/', views.ProductsListView.as_view() ,name='productos'),   
        url(r'producto/new/$', views.CreateProduct.as_view(), name='new'),  
        url(r'producto/(?P<pk>[0-9]+)/$', views.UpdateProduct.as_view( ) , name='update'),  
        url(r'producto/(?P<pk>[0-9]+)/delete', views.DeleteProduct.as_view( ) , name='delete'),
]
