from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Tarea
from .forms import TareaForm


class seleccionarTareas(View):
    def get(self, request):
        tareas = Tarea.objects.all()
        return render(request, 'tareas/tarea_list.html', {'tareas': tareas})   
    
class crearTareas(View):
    def get(self, request):
        form = TareaForm()
        return render(request, 'tareas/tarea_form.html', {'form': form})

    def post(self, request):
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea-list')
        return render(request, 'tareas/tarea_form.html', {'form': form})
    
class vistaDetalladaTareas(View):
     def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        return render(request, 'tareas/tarea_detail.html', {'tarea': tarea})
    
class actualizarTareas(View):
    def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        form = TareaForm(instance=tarea)
        return render(request,"tareas/tarea_form.html", {"form": form})
    
    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea-list')
        return render(request, 'tareas/tarea_form.html', {'form': form})
    
class EliminarTarea(View):
    def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        return render(request, 'tareas/tarea_confirm_delete.html', {'tarea': tarea})

    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        tarea.delete()
        return redirect('tarea-list')
    
     
    

   

