from django.shortcuts import render

def inicio(request):
    return render(request, 'pag/inicio.html')

def tarea_list(request):
    return render(request, 'pag/tarea_list.html')

def lisTareas(request):
    return render(request, 'lisTareas/index.html')

def CrearTarea(request):
    return render(request, 'tareas/crear.html')