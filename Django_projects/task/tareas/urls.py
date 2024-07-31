from django.contrib import admin
from django.urls import path, include
from tareas import views  

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('tarea_list', views.tarea_list, name='tarea-list'),
    path('new/', views.tarea_create, name='tarea-create'),
    path('<int:pk>/', views.tarea_detail, name='tarea-detail'),
    path('<int:pk>/edit/', views.tarea_update, name='tarea-update'),
    path('<int:pk>/delete/', views.tarea_delete, name='tarea-delete'),
]