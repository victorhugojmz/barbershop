from django.http import HttpResponseRedirect
from django.shortcuts import render 
from forms import CitaForm
from models import Cita
# Create your views here.
def index(request):
    return render(request , 'cita_templates/cita.template.html')
def book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CitaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nombre_cliente = form.cleaned_data['nombre_cliente']
            telefono_cliente = form.cleaned_data['telefono_cliente']
            direccion = form.cleaned_data['direccion']
            fecha= form.cleaned_data['fecha']
            cita = form.save(commit=False)
            cita.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/citas/')
    else:
        form = CitaForm(request.GET or None)
        context = {
            "form": form 
        }
        return render(request, 'cita_templates/cita_form.html',context)