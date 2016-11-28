from django.shortcuts import render
from forms import VentaForm
def index_citas(request):
    return render(request, 'ventas/index.ventas.html',{})
def genera_venta(request):
    if not request.user.is_authenticated:
        return render(request,'index/index.template.html',{})
    else:    
        form = VentaForm(request.POST or None)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.save()
            return render(request, 'ventas/venta.details.template.html', {'venta': venta})
        context = {
            "form": form
        }
        return render(request,'ventas/venta_form.html',context)