from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('CRUD/', views.CRUD, name='CRUD'),
    path('CRUD/crear/', views.crear, name='crear'),
    path('CRUD/editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
  ]
