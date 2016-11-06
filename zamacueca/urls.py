from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from index import views
app_name = 'main'
urlpatterns = [
     url(r'^', include('index.urls'), name='index'), 
     url(r'^admin/', admin.site.urls), 
     url(r'^citas/', include('cita.urls')),
     url(r'^account/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)