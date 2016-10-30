from django.views import generic 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.views.generic import View
from .models import Producto
from django.views.generic.edit import CreateView ,  DeleteView , UpdateView 

class IndexView(generic.ListView):
    template_name = 'productos/productos.template.html'
    def get_queryset(self):
        return Producto.objects.all()
class DetailView(generic.DetailView):
      model = Producto
      template_name = 'productos/details.template.html'
