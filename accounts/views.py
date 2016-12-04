import os 
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import ImageReader
from django.conf import settings
from django.shortcuts import render , redirect
from django.contrib.auth import (authenticate, login , get_user_model,logout)
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import UserLoginForm , UserRegistrationForm
from ventas.models import Venta
from decimal import Decimal
#Login User View 
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
#View for user details in wp
def user_account(request):
    if not request.user.is_authenticated():
       return render(request,"index/index.template.html",{})
    else:  
        return render(request,"account/user.details.html",{})
#View for logging_out
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
#View that generates PDF reports
def user_reports(request): 
    query = Venta.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=Reporte.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize = landscape(letter))
    company_logo = ImageReader('https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/13620115_781305875305339_3498004211207373370_n.jpg?oh=a354baeaead81f302d0efd2e87750956&oe=58D071A4')
    c.setLineWidth(.3)
    c.drawImage(company_logo,285,520,width=200,height=75,mask=None)
    c.setFont('Helvetica-Bold',20)
    c.drawString(30,475,'Reporte de ventas')
    c.setFont('Helvetica',18)
    c.drawString(610,475,"Diciembre")
    c.line(30,460,760,460)
    c.setFont('Helvetica-Bold',20)
    altura = 420
    c.drawString(30+10,altura,"Barbero")
    c.drawString(200+10,altura,"Total")
    c.drawString(340+10,altura,"Fecha")
    c.drawString(460+10,altura,"Servicio")
    c.drawString(600+10,altura,"Comision")
    c.setFont('Helvetica',18)
    altura_inicial = 380
    two_d = Decimal(10) ** -1
    linea = 30
    linea_final = linea + 700
    suma= 0 
    comision = 0
    comisiones= 0
    for q in query:
        comision = Decimal(q.total_venta).quantize(two_d) * Decimal(0.20).quantize(two_d)
        c.drawString(30,altura_inicial,str(q.barbero))
        c.drawString(200,altura_inicial,'$'+ str(q.total_venta) + 'MXN')
        c.drawString(340,altura_inicial,str(q.fecha_venta.date()))
        c.drawString(460,altura_inicial,str(q.servicio))
        c.drawString(600,altura_inicial,'$'+ str(comision)+ 'MXN')
        c.line(linea,altura_inicial-10,linea_final,altura_inicial-10)
        altura_inicial -=30
        suma += int(q.total_venta) 
        comisiones += int(comision) 
    c.drawString(30,altura_inicial-20,"Ganancias Netas " + "$" + str(suma-comisiones)+ "MXN")
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response