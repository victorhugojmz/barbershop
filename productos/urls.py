from django.conf.urls import include, url 
from . import views
app_name = 'productos'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'producto/new/$',views.CreateProduct.as_view(), name='new'),  
    url(r'producto/(?P<pk>[0-9]+)/$', views.UpdateProduct.as_view( ) , name='update'),  
    url(r'producto/(?P<pk>[0-9]+)/delete', views.DeleteProduct.as_view( ) , name='delete'),        
]