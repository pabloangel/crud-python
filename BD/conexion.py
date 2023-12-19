import mysql.connector
from mysql.connector import Error 

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'universidad'
            )
        except Error as ex:
            print("Error al internar la conexion {0}".format(ex))

    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY Nombre ASC")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar la conexion {0}".format(ex))

    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "INSERT INTO curso (Codigo, Nombre, Creditos) VALUES (%s, %s, %s)"
                cursor.execute(query, (curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("Curso registrado correctamente...")
            except Error as ex:
                print("Error al intentar la conexion {0}".format(ex))

    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE curso SET nombre = %s, creditos = %s WHERE codigo = %s"
                cursor.execute(query, (curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("Curso Acutalizado...")
            except Error as ex:
                print("Error al intentar la conexion {0}".format(ex))



    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE Codigo = %s"
                cursor.execute(sql, (codigoCursoEliminar,))
                self.conexion.commit()
                print("Número de filas afectadas: ", cursor.rowcount)
                if cursor.rowcount > 0:
                        print("Curso eliminado correctamente...")
                else:
                        print("No se encontró un curso con el código proporcionado.")
            except Error as ex:
                print("Error al intentar eliminar {0}".format(ex))


