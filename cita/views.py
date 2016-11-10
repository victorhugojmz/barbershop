from django.http import HttpResponse
from django.shortcuts import render 
from forms import CitaForm
# Create your views here.
def index(request):
    return render(request , 'cita_templates/cita.template.html')
def book(request):
    form = CitaForm(request.POST or None)
    context = {
        "form": form 
    }
    return render(request, 'cita_templates/cita_form.html',context)



