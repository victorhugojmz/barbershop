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
from .models import Producto , Salida , Entrada
from .forms import (  
                    UpdateProductForm,
                    CreateProductForm,
                    SalidaForm,
                    EntradaForm
                   )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.contrib import messages
def  IndexView(request):
      form  = SalidaForm(request.POST or None)
      form2 = EntradaForm(request.POST or None)
      queryset_list = Producto.objects.all()
      context = {
                    "object_list": queryset_list,
                    "form": form,
                    "fe": form2
      }
      if request.method == 'POST':
            form  = SalidaForm(request.POST)
            form2 = EntradaForm(request.POST)
            if 'salida' in request.POST:
                  form  = SalidaForm(request.POST)
                  if form.is_valid():
                        barbero = form.cleaned_data['barbero']
                        id_producto = form.cleaned_data['id_producto']
                        cantidad = form.cleaned_data['cantidad']
                        producto_object = Producto.objects.get(pk=id_producto)
                        producto_object.stock_producto = F('stock_producto') - cantidad
                        producto_object.save()
                        salida = form.save(commit=False)
                        salida.save()
                        return HttpResponseRedirect('productos/salidas/historial/')
            elif 'entrada' in request.POST:
                  form2 = EntradaForm(request.POST or None)
                  if form2.is_valid():
                        id_producto = form2.cleaned_data['id_producto']
                        cantidad = form2.cleaned_data['cantidad']
                        proveedor = form2.cleaned_data['proveedor']
                        producto_object = Producto.objects.get(pk=id_producto)
                        producto_object.stock_producto = F('stock_producto') + cantidad
                        producto_object.save()
                        entrada = form2.save(commit=False)
                        entrada.save()
                        return HttpResponseRedirect('productos/entradas/historial/')
      elif request.method == 'GET':
            queryset_list = Producto.objects.all()
            query = request.GET.get("q")
            if query: 
                  queryset_list  = queryset_list.filter(nombre_producto__icontains = query)
            context = {
                    "object_list": queryset_list,
                    "form": form,
                    "fe": form2
            }
            return render(request,"index/productos.template.html",context)
      else:
            return render(request,"index/productos.template.html",context)
def SalidasView(request):
      salidas_queryset = Salida.objects.all()
      return render(request,"index/salidas.template.html", { "salidas" : salidas_queryset})
def EntradasView(request):
      entradas_queryset = Entrada.objects.all()
      return render(request,"index/entradas.template.html",{"entradas": entradas_queryset})
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