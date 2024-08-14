from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm, UsuarioForm


def inicio(request):
    return render(request, 'pag/inicio.html')

def nosotros (request):
    return render(request, 'pag/nosotros.html')


def CRUD(request):
    tareas = Tarea.objects.all()
    return render(request, 'CRUD/index.html', {'tareas' : tareas})

def crear(request):
    formulario= TareaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('CRUD')
    return render(request,'CRUD/crear.html', {'formulario' : formulario})

def editar(request, id   ):
    tarea = Tarea.objects.get(id=id)
    formulario = TareaForm(request.POST or None, request.FILES or None, instance=tarea)
    if formulario.is_valid() and request.POST: 
        formulario.save()
        return redirect('CRUD')
    return render(request, 'CRUD/editar.html', {'formulario': formulario})

def eliminar(request,id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('CRUD') 

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista_a_redirigir')
    else:
        form = UsuarioForm()  # Aquí se asegura que form esté definido

    return render(request, 'CRUD/registrar_usuario.html', {'form': form})



