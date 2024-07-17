import Persona

#getters setters
class Profesor(Persona):
    def __init__(self, materia, años_experiencia, universidad, nombre):
        super.nombre = nombre
        self.materia = materia
        self.años_experiencia = años_experiencia
        self.universidad = universidad

    def presentar(self):
        return f"Hola, mi nombre es {self.nombre} y soy profesor de {self.materia}, egresado de la universidad {self.universidad}."

    def aumentar_experiencia(self, años):
        self.años_experiencia += años
        return f"Ahora tengo {self.años_experiencia} años de experiencia."

# Crear una instancia de la clase Profesor usando entrada del usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
materia = input("Ingrese la materia que dicta: ")
años_experiencia = int(input("Ingrese sus años de experiencia: "))
universidad = input("Ingrese la universidad donde se graduó: ")

profesor1 = Profesor(nombre, edad, materia, años_experiencia, universidad)
profesor1.cambiarNombre("pedrito")
# usar los métodos de la clase
print(profesor1.presentar())
años_a_aumentar = int(input("Ingrese los años a aumentar de experiencia: "))
print(profesor1.aumentar_experiencia(años_a_aumentar))


#1-Crear una base de datos de tareas con 1 tabla de tareas (id,desc) en dbeaver
#2-Activar entorno virtual simpre que vaya iniciar a trabajar de nuevo 
#3-crear archivo que se llame conexion.py (1 archivo)
#4-instalar driver para mysql en python msqlclient
#5-crear clase conexionn con atributos punto 6
#6-db,host,port,user,pass atributos
#7-getConexion() crear (ejecutar la funcion conectar de mysql)

#9-crear clase tarea tasks.py (2 archivo) (agregarTarea,Consultar 1 tarea,consultar todas las tareas)
#8-como consultar los datos de una tabla de una db mysql con python tasks.py
#9-como insertar datos en una tabla de una db mysql con python tasks.py


