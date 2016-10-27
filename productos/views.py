from django.views import generic
from django.views.generic.edit import CreateView ,  DeleteView , UpdateView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.views.generic import View
from .models import Producto

class IndexView(generic.ListView):
    template_name = 'productos/productos.template.html'
    def get_queryset(self):
        return Producto.objects.all()
class DetailView(generic.DetailView):
      model = Producto
      template_name = 'productos/details.template.html'    
class CreateProduct(generic.CreateView):
      model = Producto
      fields = ['nombre_producto', 'tipo_producto' , 'marca_producto' , 'precio_unitario_producto', 'stock_producto' , 'imagen_producto'] 
class UpdateProduct(generic.UpdateView):
      model = Producto
      fields = ['nombre_producto' , 'precio_unitario_producto', 'stock_producto' ]
class DeleteProduct(generic.DeleteView):
      model = Producto
      success_url = reverse_lazy('productos:index')