from django.conf.urls import include ,url
from . import views
app_name = 'index'
urlpatterns = [
    url(r'^$', views.index , name='zamacueca'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gallery/',  views.gallery, name='gallery'),
    url(r'register/$', views.UserFormView.as_view() , name='register'), 
    url(r'login_user/$', views.login_user , name='login_user'),
    url(r'logout_user/$', views.login_user , name='logout_user'),
] 