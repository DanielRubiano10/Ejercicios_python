from django.urls import path
from . import views
from .views import Perfil


urlpatterns = [
  
path('login/', views.Login.as_view(), name='login'),
path('panel', views.Panel.as_view(), name='panel'),
path('salir', views.Salir.as_view(), name='salir'),
path('perfil/<str:modo>/<int:p>', views.Perfil.as_view(), name='perfil'),
path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),
path('perfil/<str:modo>/<int:p>', views.Perfil.as_view(), name='perfil'),
]
