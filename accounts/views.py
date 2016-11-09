from django.shortcuts import render , redirect
from django.contrib.auth import (authenticate, login , get_user_model,logout)
from .forms import UserLoginForm , UserRegistrationForm
def login_user(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username , password  = password)
        login(request, user)
        return redirect("https://www.google.com.mx/")   
    return render(request,"account/login.html",{"form": form, "title": title })
def logout_user(request): 
    logout(request)
    return render(request,"account/logout.html", {})
def register_user(request):
    form = UserRegistrationForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request,"account/registration_form.html",context)
