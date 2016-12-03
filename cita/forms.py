from django import forms
from models  import Cita
horas = (
            ("11:30:00","11:30 AM"),
            ("12:00:00","12:00 PM"),
            ("12:30:00","12:30 PM"),
            ("13:00:00","13:00 PM"),
            ("13:30:00","13:30 PM"),
            ("14:00.00","14:00 PM"),
            ("14:30:00","14:30 PM"),
            ("15:00:00","15:00 PM"),
            ("15:30:00","15:30 PM"),
            ("16:00:00","16:00 PM"),
            ("16:30:00","16:30 PM"),
            ("17:00.00","17:00 PM"),
            ("17:30:00","17:30 PM"),
            ("18:00:00","18:00 PM"),
            ("18:30:00","18:30 PM"),
            ("19:00:00","19:00 PM"),
            ("19:30:00","19:30 PM"),
            ("20:00.00","20:00 PM"),
        )
class CitaForm(forms.ModelForm):
    nombre_cliente = forms.CharField(
                     widget=forms.TextInput(
                                        attrs= {
                                            'class':'form-control nombre',
                                            'placeholder':'Nombre'
                                        })
                                    )
    telefono_cliente = forms.RegexField(
                                        widget = forms.TextInput(
                                            attrs = {
                                            'class':'form-control telefono',
                                            'placeholder':'Telefono'
                                            }),
                                        regex = r'^\+?1?\d{9,15}$',
                                        )
    direccion = forms.CharField(
                    widget=forms.TextInput(
                        attrs ={
                                    'class':'form-control direccion',
                                    'placeholder':'Direccion'
                                }))
    fecha_cita = forms.DateField(
                    widget=forms.TextInput(
                            attrs=
                                {
                                    'placeholder' : 'Escoge una fecha',
                                    'class':'form-control fecha datepicker '
                                }))
    hora_cita = forms.ChoiceField(choices=horas)
    class Meta: 
        model = Cita
        fields = (
            'nombre_cliente',
            'telefono_cliente',
            'direccion',
            'fecha_cita',
            'hora_cita'
        )
class UpdateCitaForm(forms.ModelForm):
    class Meta:    
        model = Cita
        fields  = ('fecha_cita','nombre_cliente' , 'telefono_cliente', 'direccion','hora_cita')
        widgets = { 
                'fecha_cita': forms.TextInput(
                                   attrs={
                                           'class':'form-control datepicker'
                                    }),
                'nombre_cliente': forms.TextInput(
                                    attrs={
                                            'class':'form-control',
                                            'placeholder': 'Nombre del cliente'
                                    }),
                'telefono_cliente': forms.TextInput(
                                    attrs={
                                            'class':'form-control',
                                            'placeholder': 'Telefono'
                                    }),
                'direccion' : forms.TextInput(
                                attrs={
                                            'class':'form-control',
                                            'placeholder': 'Direccion' 
                                    })
        }