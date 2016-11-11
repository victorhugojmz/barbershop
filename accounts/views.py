from django.shortcuts import render , redirect
from django.contrib.auth import (authenticate, login , get_user_model,logout)
from .forms import UserLoginForm , UserRegistrationForm
def login_user(request):
        if not request.user.is_authenticated():
            form = UserLoginForm(request.POST or None)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username = username , password  = password)
                login(request, user)
                return render(request,"index/index.template.html",{})  
            return render(request,"account/login.html",{"form": form })
        else: 
            return render(request,"index/index.template.html",{}) 
def user_account(request):
    return render(request,"account/user.details.html",{})
def logout_user(request):
    if not request.user.is_authenticated():
        return render(request,"index/index.template.html", {})
    else:
        logout(request)
        return render(request,"account/logout.html", {})
def register_user(request):
    form = UserRegistrationForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request,"account/registration_form.html",context)
