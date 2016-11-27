from django.shortcuts import (  
                                render,
                                redirect
                             )
from .models import (
                        Barbero ,
                        Galeria
                    )
from django.views import generic
from django.views.generic.edit import( 
                            CreateView,
                            DeleteView
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
class Galeria(generic.ListView):
    model = Galeria
    template_name = 'index/gallery.template.html'
class DetallesImagen(generic.DetailView):
    model = Galeria
    template_name = 'galeria/galeria.details.template.html'
class NuevaImagen(CreateView):
    model = Galeria
    success_url  =  reverse_lazy('index:gallery')
    fields = ['descripcion','titulo_imagen','imagen']
class EliminaImagen(DeleteView):
    model = Galeria
    success_url = 'index/gallery.template.html'