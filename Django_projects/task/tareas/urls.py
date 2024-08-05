from django.contrib import admin
from django.urls import path, include
from . import views
from tareas import views  
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tarea-list', views.tarea_list, name='tarea-list'),
    path('lisTareas', views.lisTareas, name='lisTareas'),
    path('CrearTarea', views.CrearTarea, name='CrearTarea'),
    
    
]