from django.views import generic
from .models import Producto
class IndexView(generic.ListView):
    template_name = 'productos/productos.template.html'
    def get_queryset(self):
        return Producto.objects.all()

class DetailView(generic.DetailView):
    model = Producto
    template_name = 'productos/details.template.html'    