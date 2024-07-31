# conexion.py
import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self, db, user, password='', host='localhost', port='3306'):
        self.db = db
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
    
    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.db,
                port=self.port
            )
            if self.conn.is_connected():
                print("Conexión exitosa a la base de datos")
            return self.conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
    
    def cerrar(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Conexión cerrada exitosamente")

# Ejemplo de uso
if __name__ == "__main__":
    conexion = Conexion(db='tareas_db', user='root', password='')
    conn = conexion.conectar()
    if conn:
        conexion.cerrar()
