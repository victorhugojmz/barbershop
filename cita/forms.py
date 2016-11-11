from django import forms
from models  import Cita
class CitaForm(forms.Form):
    nombre_cliente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    telefono_cliente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control',
                                    'placeholder':'Direccion'
                                }))
    fecha = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'placeholder' : 'Escoge una fecha',
                                    'class':'datepicker'
                                }))
    def post(nombre,direccion,fecha):
        model = Cita
        save(nombre,direccion,fecha)
    class Meta: 
        model = Cita
        fields = [ 
            'nombre_cliente',
            'telefono_cliente',
            'direccion',
            'fecha',
        ]
