from django.urls import path
from .views import seleccionarTareas, crearTareas, vistaDetalladaTareas, actualizarTareas, EliminarTarea

urlpatterns = [
    path('', seleccionarTareas.as_view(), name='tarea-list'),
    path('new/', crearTareas.as_view(), name='tarea-create'),
    path('<int:pk>/', vistaDetalladaTareas.as_view(), name='tarea-detail'),
    path('<int:pk>/edit/', actualizarTareas.as_view(), name='tarea-update'),
    path('<int:pk>/delete/', EliminarTarea.as_view(), name='tarea-delete'),
]
