from django.shortcuts import (  
                                render,
                                redirect
                             )
from django.views import generic 
from django.views.generic import View
from django.views.generic.edit import (
                                        CreateView , 
                                        DeleteView , 
                                        UpdateView
                                      )
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.template import loader
from .models import Producto
from .forms import (  
                    UpdateProductForm,
                    CreateProductForm
                   )
class IndexView(generic.ListView):
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