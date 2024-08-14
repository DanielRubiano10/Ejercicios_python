from django import forms
from .models import Tarea
from .models import Usuario

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'cedula', 'fecha_nacimiento']
        

