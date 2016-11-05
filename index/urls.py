from django.conf.urls import include ,url
from . import views
app_name = 'index'
urlpatterns = [
    url(r'^$', views.index , name='zamacueca'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gallery/',  views.gallery, name='gallery'),
    url(r'^producto/', views.IndexView.as_view(), name='index'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'producto/add/$' , views.ProductCreate.as_view( ), name="product-add"), 
    url(r'producto/(?P<pk>[0-9]+)/$' , views.ProductUpdate.as_view( ), name="product-update"), 
    url(r'producto/(?P<pk>[0-9]+)/delete/$' , views.ProductDelete.as_view( ), name="product-delete"),
] 
