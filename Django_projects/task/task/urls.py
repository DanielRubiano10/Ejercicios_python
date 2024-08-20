from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view  
from django.views.generic import RedirectView

# Define la vista de Swagger
schema_view = get_swagger_view(title='Your API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tareas.urls')),
    path('swagger/', schema_view),# Ruta para Swagger
    path('api-auth/', include('rest_framework.urls')),# Ruta para la autenticación de API
    path('', RedirectView.as_view(url='/tareas/login'))
]
