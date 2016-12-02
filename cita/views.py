#Request Handling resources
from django.http import HttpResponseRedirect
from django.shortcuts import ( 
                                render,
                                redirect
                             )
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import View 
# Rest Framework Views for REST API 
from rest_framework.views import APIView
from django.views.generic.edit import (
                                        DeleteView , 
                                        UpdateView
                                      )
from rest_framework.response import Response
from rest_framework import status
from .serializers import CitaSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
# Model forms 
from forms import CitaForm , UpdateCitaForm
# Models 
from datetime import datetime
from models import Cita


def  index(request):
    query_set_list  =  Cita.objects.filter()
    context = {
        "object_list": query_set_list
    }
    return render(request,'cita_templates/cita.template.html',context)
class DeleteCita(generic.DeleteView):
    model = Cita
    success_url  =  reverse_lazy('cita:index')
class UpdateCitaView(generic.UpdateView):
    model = Cita
    form_class = UpdateCitaForm
    success_url  =  reverse_lazy('cita:index')
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
            fecha_cita = form.cleaned_data['fecha_cita']
            cita = form.save(commit=False)
            cita.save()
            return HttpResponseRedirect('/')
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
