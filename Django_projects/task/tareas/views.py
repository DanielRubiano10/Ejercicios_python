from django.shortcuts import render
from .models import Tarea


def inicio(request):
    return render(request, 'pag/inicio.html')

def nosotros (request):
    return render(request, 'pag/nosotros.html')


def CRUD(request):
    CRUD = Tarea.objects.all()
    return render(request, 'CRUD/index.html', {'CRUD' : CRUD})

def crear(request):
    return render(request,'CRUD/crear.html')

def editar(request):
    return render(request, 'CRUD/editar.html')





