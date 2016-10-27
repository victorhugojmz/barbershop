from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def encargado(request):
     return render(request , 'encargado/encargado.html')