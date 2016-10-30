from django.conf.urls import include, url 
from . import views
app_name = 'producto'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'producto/add/$' , views.ProductCreate.as_view( ), name="product-add"), 
    #editing a view
    url(r'producto/(?P<pk>[0-9]+)/$' , views.ProductUpdate.as_view( ), name="product-update"), 
    #for deleting a view
    url(r'producto/(?P<pk>[0-9]+)/delete/$' , views.ProductDelete.as_view( ), name="product-delete"),
]