from django.conf.urls import include ,url
from . import views
app_name = 'index'
urlpatterns = [
    url(r'^$', views.index , name='zamacueca'),
    url(r'^nosotros/$', views.about, name='about'),
    url(r'^galeria/$',  views.gallery, name='gallery'),
] 