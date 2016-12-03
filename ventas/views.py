from django.shortcuts import render
from forms import VentaForm
from models import Venta
def index_citas(request):
    object_list = Venta.objects.all() 
    context = {
        "object_list": object_list
    }
    return render(request, 'ventas/index.ventas.html',context)
def genera_venta(request):
    if not request.user.is_authenticated:
        return render(request,'index/index.template.html',{})
    else:    
        form = VentaForm(request.POST or None)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.save()
            return render(request,'ventas/index.ventas.html')
        context = {
            "form": form
        }
        return render(request,'ventas/venta_form.html',context)