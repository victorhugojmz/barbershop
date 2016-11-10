from django.conf.urls import include, url
from . import views 
app_name = 'account'
urlpatterns = [
    url(r'register_user/$', views.register_user , name='register'), 
    url(r'login_user/$', views.login_user , name='login_user'),
    url(r'logout_user/$', views.logout_user , name='logout_user'),
 ]