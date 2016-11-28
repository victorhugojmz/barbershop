from django import forms
from models  import Cita
class CitaForm(forms.ModelForm):
    nombre_cliente = forms.CharField(
                    widget=forms.TextInput(
                                        attrs= {
                                            'class':'form-control',
                                            'placeholder':'Nombre'
                                        })
                                    )
    telefono_cliente = forms.RegexField(
                                        widget = forms.TextInput(
                                            attrs = {
                                            'class':'form-control',
                                            'placeholder':'Telefono'
                                            }),
                                        regex = r'^\+?1?\d{9,15}$',
                                        )
    direccion = forms.CharField(
                    widget=forms.TextInput(
                        attrs ={
                                    'class':'form-control',
                                    'placeholder':'Direccion'
                                }))
    fecha_cita = forms.DateField(
                    widget=forms.TextInput(
                            attrs=
                                {
                                    'placeholder' : 'Escoge una fecha',
                                    'class':'form-control datepicker'
                                }))
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
        fields  = ('fecha_cita','nombre_cliente' , 'telefono_cliente', 'direccion')
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