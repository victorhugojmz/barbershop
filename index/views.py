from django.shortcuts import (  
                                render,
                                redirect
                             )
from .models import (
                        Barbero ,
                        Galeria
                    )
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.template import loader
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
    imagenes =  Galeria.objects.all()
    template = loader.get_template('index/gallery.template.html')
    context = {
        'imagenes' : imagenes
    }  
    return HttpResponse(template.render(context,request))