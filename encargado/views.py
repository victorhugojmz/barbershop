from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate , login 
from django.views.generic import View
from django.views import generic
from productos.models import Producto
# Create your views here.
def encargado(request):
     return render(request , 'encargado/encargado.html')
class ProductsListView(generic.ListView):
      template_name = 'encargado/encargado.productos.template.html'
      def get_queryset(sellf):
         return Producto.objects.all()
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