from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tareas/', views.tarea_list, name='tarea-list'),
    path('tareas/<int:pk>/', views.tarea_detail, name='tarea-detail'),
    path('tareas/nueva/', views.tarea_create, name='tarea-create'),
    path('tareas/<int:pk>/editar/', views.tarea_update, name='tarea-update'),
    path('tareas/<int:pk>/eliminar/', views.tarea_delete, name='tarea-delete'),
]
