from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    cedula = models.CharField(max_length=20, unique=True, verbose_name='Cédula')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    
    def __str__(self):
        return f"{self.nombre} - {self.cedula}"
    
class Tarea(models.Model):
    id = models.AutoField(primary_key=True) #campo auto incremental 
    descripcion = models.CharField(max_length=255, verbose_name='Descripción')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas')
             
    def __str__(self):
        fila="Titulo: " + self.descripcion + "-" + "Descripcion: " + str(self.completada)
        return fila 



    
    
    
    
    

    