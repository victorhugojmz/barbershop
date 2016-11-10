from django import forms
from models  import Cita
class CitaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    fecha = forms.DateField()
    class Meta: 
        model = Cita
        fields = [ 
            'nombre',
            'nombre_cliente',
            'telefono_cliente',
            'direccion',
            'fecha',
        ]