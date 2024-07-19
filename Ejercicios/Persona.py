class Persona:
    def __init__(self, nombre, edad,apellido,ojos=2):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ojos = ojos
    
    #setter    
    def setName(self,nuevoNombre):
        self.nombre = nuevoNombre
    #getter
    def getName(self):
        return self.nombre    
        
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre} y soy profesor de {self.materia}, egresado de la universidad {self.universidad}."

    def aumentar_experiencia(self, años):
        self.años_experiencia += años
        return f"Ahora tengo {self.años_experiencia} años de experiencia."
