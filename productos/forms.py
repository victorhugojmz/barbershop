from django import forms
from models import Producto , Salida
marcas = (
            ("SUA","Suavecito"),
            ("MAL","Malo"),
            ("WRN","WRONG"),
    )
tipos = {
     ("ACE","Aceite"),
     ("AFS","After Shave"),
     ("BFS","Before Shave"),
     ("BAL","Balsamo"),
     ("PEI","Peine"),
}
class UpdateProductForm(forms.ModelForm):
     class Meta:
        model = Producto
        fields  = ('nombre_producto' , 'tipo_producto' , 'precio_unitario_producto', 'stock_producto', 'descripcion_producto','imagen_producto')
        widgets = { 
            'nombre_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Nombre del producto'
                                }),
            'precio_unitario_producto' : forms.NumberInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Precio en MXN' 
                                }),
            'stock_producto' :  forms.NumberInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Cantidad de producto'
                                }),
            'descripcion_producto': forms.Textarea(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Descripcion del producto'
                                }),
            'imagen_producto': forms.FileInput(
                            attrs= {
                                'class': 'form-control'
                            }
            )
        }
class CreateProductForm(forms.ModelForm):
     class Meta:
        model = Producto
        fields  = ('nombre_producto' , 'tipo_producto' , 'marca_producto' , 'precio_unitario_producto', 'stock_producto', 'descripcion_producto','imagen_producto')
        widgets = { 
            'nombre_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Nombre del producto'
                                }),
            'tipo_producto': forms.Select(
                            choices= tipos, 
                            attrs= 
                            {
                                'class': 'form-control'
                            }),
            'marca_producto': forms.Select(
                        choices= marcas, 
                        attrs= 
                        {
                            'class': 'form-control'
                        }),
            'precio_unitario_producto' : forms.NumberInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Precio en MXN' 
                                }),
            'stock_producto' :  forms.NumberInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Cantidad de producto'
                                }),
            'descripcion_producto': forms.Textarea(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Descripcion del producto'
                                }),
            'imagen_producto': forms.FileInput(
                            attrs={
                                'class':'btn btn-success'
                            })
        } 
class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ('barbero','id_producto','cantidad','concepto')