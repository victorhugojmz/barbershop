from django.shortcuts import render
def index_citas(request):
    return render(request, 'ventas/index.ventas.html',{})