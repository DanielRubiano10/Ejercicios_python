from django.db import models

# Create your models here.
class Tarea (models.Model):
    id = models.AutoField(primary_key=True) #campo auto incremental 
    descripcion = models.CharField(max_length=255)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        fila="Titulo: " + self.descripcion + "-" + "Descripcion: " + str(self.completada)
        return fila 
