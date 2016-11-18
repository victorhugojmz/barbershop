from django import forms
from models import Producto
class UpdateProductForm(forms.ModelForm):
     class Meta:
        model = Producto
        fields  = ('nombre_producto' , 'tipo_producto' , 'marca_producto' , 'precio_unitario_producto', 'stock_producto', 'descripcion_producto')
        widgets = { 
            'nombre_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Nombre del producto'
                                }),
            'tipo_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Tipo de producto'
                                }),
            'marca_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Marca'
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
                                })
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
            'tipo_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Tipo de producto'
                                }),
            'marca_producto': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder': 'Marca'
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