# tasks.py
from conexion import Conexion

class TaskManager:
    def __init__(self, db):
        self.db = db
        self.conn = Conexion(db=db, user="root", password="tu_contraseña").getConexion()  # Usa la contraseña correcta

    def agregar_tarea(self, descripcion):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO tareas (descripcion) VALUES (%s)", (descripcion,))
                self.conn.commit()
                print("Tarea agregada con éxito.")
            except Exception as e:
                print(f"Error al agregar la tarea: {e}")
            finally:
                cursor.close()
        else:
            print("No se pudo conectar a la base de datos")

    def consultar_tarea(self, tarea_id):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM tareas WHERE id = %s", (tarea_id,))
                tarea = cursor.fetchone()
                if tarea:
                    print(f"Tarea encontrada: {tarea}")
                else:
                    print("Tarea no encontrada.")
            except Exception as e:
                print(f"Error al consultar la tarea: {e}")
            finally:
                cursor.close()
        else:
            print("No se pudo conectar a la base de datos")

    def consultar_todas_las_tareas(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM tareas")
                tareas = cursor.fetchall()
                if tareas:
                    print("Todas las tareas:")
                    for tarea in tareas:
                        print(tarea)
                else:
                    print("No hay tareas.")
            except Exception as e:
                print(f"Error al consultar todas las tareas: {e}")
            finally:
                cursor.close()
        else:
            print("No se pudo conectar a la base de datos")

    def __del__(self):
        if self.conn:
            Conexion(db=self.db).cerrar(self.conn)

# Ejemplo de uso
if __name__ == "__main__":
    task_manager = TaskManager(db="tareas_db")  # Asegúrate de que el nombre de la clase está escrito correctamente
    task_manager.agregar_tarea("Comprar leche")
    task_manager.consultar_tarea(1)
    task_manager.consultar_todas_las_tareas()
