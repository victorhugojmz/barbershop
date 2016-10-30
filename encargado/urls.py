from django.conf.urls import include ,url
from . import views
app_name = 'encargado'
urlpatterns = [
        url(r'^$', views.encargado ,  name='index'),    
        url(r'register/$', views.UserFormView.as_view() , name='register'), 
        url(r'login_user/$', views.login_user , name='login_user'),
        url(r'logout_user/$', views.login_user , name='logout_user'),          
]
