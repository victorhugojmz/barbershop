from django.shortcuts import render,  get_object_or_404,redirect 
from django.http import HttpResponse
from django.template import loader
from .models import Barbero ,  Imagen
from django.contrib.auth.decorators import login_required
from django.views.generic import View
# Create your views here.
def index(request):
    return render(request , 'index/index.template.html')
def about(request): 
    barberos = Barbero.objects.all()
    template = loader.get_template('index/about.template.html')
    context = {
        'barberos' : barberos
    }
    return HttpResponse(template.render(context ,request))
def gallery(request): 
    imagenes =  Imagen.objects.all()
    template = loader.get_template('index/gallery.template.html')
    context = {
        'imagenes' : imagenes
    }  
    return HttpResponse(template.render(context,request))