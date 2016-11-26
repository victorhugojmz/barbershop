from django.shortcuts import (  
                                render,
                                redirect
                             )
from .models import (
                        Barbero ,
                        Galeria
                    )
from django.views.generic import ListView , CreateView,DeleteView
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
class Galeria(ListView):
    model = Galeria
    template_name = 'index/gallery.template.html'
class NuevaImagen(CreateView):
    class Meta: 
        model = Galeria
        fields = ['descripcion','titulo_imagen','imagen']
