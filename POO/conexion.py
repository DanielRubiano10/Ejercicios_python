# conexion.py
import mysql.connector

class Conexion:
    def __init__(self, db, user="root", password=None, host="localhost", port=3306):
        self.db = db
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
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

    def cerrar(self, conexion):
        if conexion:
            conexion.close()
            print('Conexion cerrada.')

# Prueba de conexión
if __name__ == "__main__":
    Conexion_db = Conexion(db="tareas_db", user="root", password="tu_contraseña")
    Conexion = Conexion_db.getConexion()
    if Conexion:
        cursor = Conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla)
        cursor.close()
        Conexion_db.cerrar(Conexion)
    else:
        print("No se pudo conectar a la base de datos")
