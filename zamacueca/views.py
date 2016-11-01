from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.shortcuts import render,  get_object_or_404,redirect
from django.views.generic import View
class UserFormView(View):
      form_class = UserForm
      template_name = 'user/registration_form.html'
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
                              return redirect('main:index')
            return  render(request, self.template_name, { 'form' : form })
def login_user(request):
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None:
             if user.is_active:
                return render(request, 'index/index.template.html', {'username' : request.user.username})
             else:
                return render(request, 'user/login.html', {'error_message': 'Your account has been disabled'})
         else:
             return render(request, 'user/login.html', {'error_message': 'Invalid login'})
    return render(request, 'user/login.html')
def logout_user(request):
    logout(request)
    return redirect('index')
