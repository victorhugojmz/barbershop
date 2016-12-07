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
from django.contrib.auth.mixins import LoginRequiredMixin
def  IndexView(request):
      queryset_list = Producto.objects.all()
      query = request.GET.get("q")
      if query: 
            queryset_list  = queryset_list.filter(nombre_producto__icontains = query)
      context = {
            "object_list" : queryset_list
      }
      return render(request,"index/productos.template.html",context)
      #template_name = 'index/productos.template.html'
def  salidaView(request):
      return render(request,"index/salida.form.html",{})
class DetailView(generic.DetailView):
      model = Producto
      template_name = 'index/details.template.html'
class ProductCreate(LoginRequiredMixin,CreateView):
      login_url = 'account/login_user/'
      redirect_field_name = 'account/login_user/'
      model = Producto 
      form_class  = CreateProductForm
      success_url  =  reverse_lazy('productos:index')      
class ProductUpdate(LoginRequiredMixin,UpdateView):
      login_url = 'account/login_user/'
      redirect_field_name = 'account/login_user/'
      model = Producto 
      form_class = UpdateProductForm
      success_url  =  reverse_lazy('productos:index')
class ProductDelete(DeleteView): 
      model = Producto 
      success_url  =  reverse_lazy('productos:index')