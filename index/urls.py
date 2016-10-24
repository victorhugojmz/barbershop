from django.conf.urls import include ,url
from . import views
app_name = 'index'
urlpatterns = [
    url(r'^$', views.index , name='zamacueca'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gallery/',  views.gallery, name='gallery'),
] 