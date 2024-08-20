#renderizacion de vistas al usuario 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 

from django.http import HttpResponseRedirect, HttpResponse, FileResponse #para redirigir a otras pag
from .forms import * #el formulario de login
from django.views import View #crea vistas basadas en sub clases
from django.contrib.auth import authenticate, login, logout #autentificacion de usuario inicio sesion
from django.contrib.auth.mixins import LoginRequiredMixin#verifica si el usaurio esta logeado
from .forms import UsuarioFormulario, LoginFormulario, ClaveFormulario
from .models import Producto, Usuario

#modelos
from .models import *
from .funciones import * #funciones personalizadas

#Interfaz de inicio de sesion----------------------------------------------------#
class Login(View):
    #Si el usuario ya envio el formulario por metodo post
    def post(self,request):
        form = LoginFormulario(request.POST)
        # Revisa si es valido:
        if form.is_valid():
            usuario = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            logeado = authenticate(request, username=usuario, password=clave)
            if logeado is not None:
                login(request,logeado)
                return redirect('inventario/panel')
            
            else:
                return render(request, 'inventario/login.html', {'form': form})
    
    # Si se llega por GET crearemos un formulario en blanco
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('panel')
        
        form = LoginFormulario()
        return render(request, 'inventario/login.html', {'form': form})
 #Fin de vista---------------------------------------------------------------------#   
 
 

#Panel de inicio y vista principal------------------------------------------------#
class Panel(LoginRequiredMixin, View):
    #De no estar logeado, el usuario sera redirigido a la pagina de Login
    #Las dos variables son las pagina a redirigir y el campo adicional, respectivamente
    login_url = '/inventario/login'
    redirect_field_name = None

    def get(self, request):
        from datetime import date
        #Recupera los datos del usuario despues del login
        contexto = {'usuario': request.user.username,
                    'id_usuario':request.user.id,
                   'nombre': request.user.first_name,
                   'apellido': request.user.last_name,
                   'correo': request.user.email,
                   'fecha':  date.today(),
                   'productosRegistrados' : Producto.numeroRegistrados(),
                   'usuarios': Usuario.numeroUsuarios('usuario')
        }
        return render(request, 'inventario/panel.html',contexto)
#Fin de vista----------------------------------------------------------------------#


#Maneja la salida del usuario------------------------------------------------------#
class Salir(LoginRequiredMixin, View):
    #Sale de la sesion actual
    login_url = 'inventario/login'
    redirect_field_name = None

    def get(self, request):
        logout(request)
        return render(request, '/inventario/login')
#Fin de vista----------------------------------------------------------------------#

#Muestra el perfil del usuario logeado actualmente---------------------------------#
class Perfil(LoginRequiredMixin, View):
    login_url = 'inventario/login'
    redirect_field_name = None

    def get(self, request, modo, p):
        user = get_object_or_404(Usuario, id=p)

        if modo == 'editar':
            if not self._puede_editar(request, user):
                return redirect('/inventario/perfil/ver/%s' % p)

            form = UsuarioFormulario(instance=user)
            contexto = {'form': form, 'modo': 'editar', 'nombreUsuario': user.username}
            return render(request, 'inventario/perfil/perfil.html', contexto)

        elif modo == 'clave':
            if not self._puede_cambiar_clave(request, user):
                return redirect('/inventario/perfil/ver/%s' % p)

            form = ClaveFormulario()
            contexto = {'form': form, 'modo': 'clave', 'nombreUsuario': user.username}
            return render(request, 'inventario/perfil/perfil.html', contexto)

        elif modo == 'ver':
            contexto = {'perfil': user}
            return render(request, 'inventario/perfil/verPerfil.html', contexto)

    def post(self, request, modo, p):
        user = get_object_or_404(Usuario, id=p)

        if modo == 'editar':
            form = UsuarioFormulario(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Perfil actualizado exitosamente.')
                return redirect('/inventario/perfil/ver/%s' % user.id)
            else:
                return render(request, 'inventario/perfil/perfil.html', {'form': form, 'modo': 'editar'})

        elif modo == 'clave':
            form = ClaveFormulario(request.POST)
            if form.is_valid():
                clave_nueva = form.cleaned_data['clave_nueva']
                repetir_clave = form.cleaned_data['repetir_clave']
                if clave_nueva == repetir_clave:
                    user.set_password(clave_nueva)
                    user.save()
                    messages.success(request, 'Clave cambiada correctamente!')
                    return redirect("/inventario/login")
                else:
                    messages.error(request, 'Las claves no coinciden.')
            return redirect("/inventario/perfil/clave/%s" % p)

    def _puede_editar(self, request, user):
        if request.user.id == user.id or request.user.is_superuser:
            return True
        messages.error(request, 'No tienes permiso para editar este perfil.')
        return False

    def _puede_cambiar_clave(self, request, user):
        if request.user.is_superuser or request.user.id == user.id:
            return True
        messages.error(request, 'No tienes permiso para cambiar la clave de este usuario.')
        return False
#Fin de vista----------------------------------------------------------------------#

#mostrar productos-----------------------------------------------------------------#
class ListarProductos(LoginRequiredMixin, View):
    login_url = '/inventario/login'
    redirect_field_name = None
    
    def get(self, request):
        Productos = Producto.objects.all()
        contexto ={'tabla':Productos}
        return render(request, 'inventario/producto/listarProductos.html', contexto)
#Fin de vista----------------------------------------------------------------------#

#Elimina usuarios, productos, clientes o proveedores----------------------------
class Eliminar(LoginRequiredMixin, View):
    login_url = '/inventario/login'
    redirect_field_name = None

    def get(self, request, modo, p):

        if modo == 'producto':
            prod = Producto.objects.get(id=p)
            prod.delete()
            messages.success(request, 'Producto de ID %s borrado exitosamente.' % p)
            return HttpResponseRedirect("/inventario/listarProductos")         
           
        elif modo == 'usuario':
            if request.user.is_superuser == False:
                messages.error(request, 'No tienes permisos suficientes para borrar usuarios')  
                return HttpResponseRedirect('/inventario/listarUsuarios')
            else:
                usuario = Usuario.objects.get(id=p)
                usuario.delete()
                messages.success(request, 'Usuario de ID %s borrado exitosamente.' % p)
                return HttpResponseRedirect("/inventario/listarUsuarios")        


#Fin de vista-------------------------------------------------------------------   

        