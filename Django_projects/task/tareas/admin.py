from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import LoginFormulario
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    add_form = LoginFormulario
    #configuracion solo para el modelo usuario.
    model = Usuario
    list_display = ['email', 'username',]

admin.site.register(Usuario, UsuarioAdmin)#se registra el modelo 