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
"""class IndexView(generic.ListView):
    template_name = 'index/productos.template.html'
    def get_queryset(self):
        return Producto.objects.all()
class DetailView(generic.DetailView):
      model = Producto
      template_name = 'index/details.template.html'
class ProductCreate(CreateView):
      model = Producto 
      form_class  = CreateProductForm
      success_url  =  reverse_lazy('index:index')      
class ProductUpdate(UpdateView):
      model = Producto 
      form_class = UpdateProductForm
      success_url  =  reverse_lazy('index:index')
class ProductDelete(DeleteView): 
      model = Producto 
      success_url  =  reverse_lazy('index:index')
# Create your views here
"""
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