from django.views import generic
from django.views.generic.edit import CreateView ,  DeleteView , UpdateView 
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login 
from django.views.generic import View
from .models import Producto
from .forms import UserForm

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
class UserFormView(View):
      form_class = UserForm
      template_name = 'productos/registration_form.html'
      #displays blank form
      def get(self,request):
            form = self.form_class(None)
            return render(request, self.template_name, {'form' : form })
      #process form data 
      def post(self,request):
            form = self.form_class(request.POST)

            if form.is_valid( ):
                  user = form.save(commit = False)
                  #Cleaned normalized data
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']
                  user.set_password(password)
                  user.save( )
                  user = authenticate(username= username, password = password)
                  if user is not None:
                        
                        if user.is_active:
                              login(request, user)
                              return redirect('productos:index')
            return  render(request, self.template_name, { 'form' : form })