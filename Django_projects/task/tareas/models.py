from django.db import models
from django.contrib.auth.models import AbstractUser


# MODELOS

#--------------------------------USUARIO------------------------------------------------
class Usuario(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Cambia 'custom_user_set' a lo que prefieras
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_permission_set',  # Cambia 'custom_permission_set' a lo que prefieras
        blank=True
    )
    #id
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    nivel = models.PositiveIntegerField(choices=[(1, 'Nivel 1'), (2, 'Nivel 2')])
    
    @classmethod
    def numeroUruarios(cls, tipo):
        return cls.objects.filter(tipo=tipo).count()
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['id']
        
class Opciones(models.Model):
    #id
    moneda = models.CharField(max_length=20, null=True)
    valor_iva = models.IntegerField(unique=True)   
    
           
#-------------------------------PRODUCTO------------------------------------------------
class Producto(models.Model):
    #id
    decisiones =  [('1','Unidad'),('2','Kilo'),('3','Litro'),('4','Otros')]
    descripcion = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    categoria = models.CharField(max_length=20,choices=decisiones, default='General')
    tiene_iva = models.BooleanField(default=False)
    
    @classmethod
    def numeroRegistrados(cls):
        return cls.objects.all().count()
    
    @classmethod
    def productosRegistrados(self):
        objetos = self.objects.all().order_by('descripcion')
        return objetos
    