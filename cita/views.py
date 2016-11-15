from django.http import HttpResponseRedirect
from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CitaSerializer
from forms import CitaForm
from models import Cita
# Create your views here.
def index(request):
    return render(request , 'cita_templates/cita.template.html')
def book(request):
    form = CitaForm(request.POST or None)
    context = {
        
          "form": form 
    }
    if request.method == 'POST':
        form = CitaForm(request.POST or None)
        if form.is_valid():
            nombre_cliente = form.cleaned_data['nombre_cliente']
            telefono_cliente = form.cleaned_data['telefono_cliente']
            direccion = form.cleaned_data['direccion']
            fecha= form.cleaned_data['fecha']
            cita = form.save(commit=False)
            cita.save()
            return HttpResponseRedirect('/citas')
    else:    
        form = CitaForm(request.POST or None)
        context = {
          "form": form 
        }
    return render(request, 'cita_templates/cita_form.html',context)
class ListaDeCitas(APIView):
    def get(self , request):
        citas  =  Cita.objects.all()
        serializer = CitaSerializer(citas, many=True)
        return Response(serializer.data)
