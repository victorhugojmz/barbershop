from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate , login
from django.contrib.auth import logout
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from productos.models import Producto
from django.views.generic.edit import CreateView ,  DeleteView , UpdateView 
# Create your views here.
def encargado(request):
      if request.user.is_authenticated():
            return 
      return render(request , 'encargado/encargado.html')
class ProductsListView(generic.ListView):
      template_name = 'encargado/encargado.productos.template.html'
      def get_queryset(sellf):
         return Producto.objects.all()
class ProductDetailView(generic.DetailView):
      model = Producto
      template_name = 'encargado/encargado.producto.details.template.html' 
class CreateProduct(generic.CreateView):
      model = Producto
      fields = ['nombre_producto', 'tipo_producto' , 'marca_producto' , 'precio_unitario_producto', 'stock_producto' , 'imagen_producto'] 
class UpdateProduct(generic.UpdateView):
      model = Producto
      fields = ['nombre_producto' , 'precio_unitario_producto', 'stock_producto' ]
class DeleteProduct(generic.DeleteView):
      model = Producto
      success_url = reverse_lazy('encargado:productos')
class UserFormView(View):
      form_class = UserForm
      template_name = 'encargado/registration_form.html'
      #displays blank f+orm
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
def login_user(request):
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None:
             if user.is_active:
                return render(request, 'encargado/encargado.html', {'username' : request.user.username})
             else:
                return render(request, 'encargado/login.html', {'error_message': 'Your account has been disabled'})
         else:
             return render(request, 'encargado/login.html', {'error_message': 'Invalid login'})
    return render(request, 'encargado/login.html')
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'encargado/login.html', context)
