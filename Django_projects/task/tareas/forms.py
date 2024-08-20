from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Producto, Usuario


class LoginFormulario(forms.Form):#formulario de autenticacion
    username = forms.CharField(label="Tu nombre de usuario",widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario',
        'class': 'form-control underlined', 'type':'text','id':'user'}))

    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
        'class': 'form-control underlined', 'type':'password','id':'password'}))
        
class ProductoFormulario(forms.ModelForm):#formulario que permite a los usuarios agregar o editar produtos 
    precio = forms.DecimalField(
        min_value = 0,
        label = 'Precio',
        widget = forms.NumberInput(
        attrs={'placeholder': 'Precio del producto',
        'id':'precio','class':'form-control'}),
        )
    class Meta:
        model = Producto
        fields = ['descripcion','precio','categoria','tiene_iva']
        labels = {
        'descripcion': 'Nombre',
        'tiene_iva': 'Incluye IVA?'
        }
        widgets = {
        'descripcion': forms.TextInput(attrs={'placeholder': 'Nombre del producto',
        'id':'descripcion','class':'form-control'} ),
        'categoria': forms.Select(attrs={'class':'form-control','id':'categoria'}),
        'tiene_iva': forms.CheckboxInput(attrs={'class':'checkbox rounded','id':'tiene_iva'}) 
        }


class UsuarioFormulario(forms.ModelForm):#formulario que permite gestionar los datos del usuario (nombre,apellido,email)
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'nivel']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class ClaveFormulario(forms.Form):#formulario que permite a los usuarios cambiar su contraseña
    clave_nueva = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nueva clave'}))
    repetir_clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repetir clave'}))
