#----------------------------FUNCIONES DE AYUDA Y COMPLEMENTO--------------------------------------------------

from .models import Producto, Opciones
from decimal import Decimal


def obtenerIdProducto(descripcion):
    id_producto = Producto.objects.get(descripcion=descripcion)
    resultado = id_producto.id

    return resultado

def obtenerProducto(idProducto):
    producto = Producto.objects.get(id=idProducto)      
    return producto

def usuarioExiste(Usuario,buscar,valor):
    filtro = {buscar: valor}
    return  Usuario.objects.filter(**filtro).exists()