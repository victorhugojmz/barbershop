import os 
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm 
from django.conf import settings
from django.shortcuts import render , redirect
from django.contrib.auth import (authenticate, login , get_user_model,logout)
from django.core.mail import send_mail
from django.http import HttpResponse
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
    if not request.user.is_authenticated():
       return render(request,"index/index.template.html",{})
    else:  
        return render(request,"account/user.details.html",{})
def logout_user(request):
    if not request.user.is_authenticated():
        return render(request,"index/index.template.html", {})
    else:
        logout(request)
        return render(request,"account/logout.html", {})
def register_user(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
        subject = 'Thank You'
        message = 'Welcome'
        from_email = settings.EMAIL_HOST_USER 
        to_list = [user.email, settings.EMAIL_HOST_USER ]
        send_mail(subject,message,from_email,to_list,fail_silently=True) 
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'account/user.details.html', {})
    context = {
        "form": form,
    }
    return render(request, 'account/registration_form.html', context)
def user_reports(request): 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=Reporte.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize = A4)
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,770,'Reporte')
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response