#ejemplo de conexion a una base de datos 
import mysql.connector

# Establecemos la conexión
class Conexion:
    def __init__(self, db, user="root", password="root", host="localhost", database="tareas_db", port="3306"):
        self.db = db
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        
    def getConexion(self):
        config = {
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port,
            "database": self.db
        }
        try:
            conexion = mysql.connector.connect(**config)
            print("Conexion exitosa a la base de datos")
            return conexion
        except mysql.connector.Error as err:
            print(f"Error de conexion: {err}")
            return None
Conexion_db = Conexion(db="tareas_db")#crear una instancia de la clase conexion
Conexion = Conexion_db.getConexion()#obtener la conexion    

if Conexion:
    cursor= Conexion.cursor()
    cursor.execute("SHOW TABLES")
    tablas= cursor.fetchall()
    print("tablas en la base de datos: ")
    for tabla in tablas:
        print(tabla)
        cursor.close()
        Conexion.close()
else:
    print("No se pudo conectar a la base de datos ")
    
    
