from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm

def inicio(request):
    return render(request, 'inicio.html')

def tarea_list(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/tarea_list.html', {'tareas': tareas})

def tarea_create(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea-list')
    else:
        form = TareaForm()
    return render(request, 'tareas/tarea_form.html', {'form': form})

def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tareas/tarea_detail.html', {'tarea': tarea})

def tarea_update(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea-list')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/tarea_form.html', {'form': form})

def tarea_delete(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect('tarea-list')
    return render(request, 'tareas/tarea_confirm_delete.html', {'tarea': tarea})