from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm

def inicio(request):
    return render(request, 'pag/inicio.html')

def nosotros (request):
    return render(request, 'pag/nosotros.html')


def CRUD(request):
    CRUD = Tarea.objects.all()
    return render(request, 'CRUD/index.html', {'CRUD' : CRUD})

def crear(request):
    formulario= TareaForm(request.POST or None)
    return render(request,'CRUD/crear.html', {'formulario' : formulario})

def editar(request):
    return render(request, 'CRUD/editar.html')





