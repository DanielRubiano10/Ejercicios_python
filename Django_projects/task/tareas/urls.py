from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('CRUD', views.CRUD, name='CRUD'),
    path('CRUD/crear', views.crear, name='crear'),
    path('CRUD/Editar', views.editar, name='editar'),
  ]
