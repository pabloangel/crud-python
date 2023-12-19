import time
import os
from BD.conexion import DAO
import Funciones

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def menuPrincipal():
    print("********** MENU PRINCIPAL **********")
    print("1. Listar Curso ")
    print("2. Registrar Curso ")
    print("3. Actualizar Curso ")
    print("4. Eliminar Curso ")
    print("5. Salir ")
    print("************************************")
    opcion = int(input("Ingrese una opcion: "))
    limpiar_pantalla()
    
    if opcion <1 or opcion >5:
        time.sleep(3)
        print("Opcion no valida, Ingrese nuevamente...")
        menuPrincipal()
    elif opcion == 5:
        print("Gracias por utilizar el sistema")
    else:
        ejecutarOpcion(opcion)
        
def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cursos= dao.listarCursos()
            if len(cursos) > 0:
                Funciones.listarCursos(cursos)
                print("************************************************************************")
                print("\n") 
                menuPrincipal()
            else:
                print("No hay cursos registrados...")
        except Exception as e:
            print("Error al listar los cursos: ", e)
    elif opcion == 2:
        curso = Funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except Exception as e:
            print("Error al registrar el curso: ", e)
    elif opcion == 3:
        try:
            cursos= dao.listarCursos()
            if len(cursos) > 0:
                curso = Funciones.pedirDatosActualizacion(cursos)
                if curso: 
                     dao.actualizarCurso(curso)
                else:
                   print("codigo de curso a actualizar no existe...\n")
            else:    
                print("No hay cursos registrados...")                
        except Exception as e:
            print("Error al eliminar el curso: ", e)
    elif opcion == 4:
        try:
            cursos= dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = Funciones.pedirDatosEliminacion(cursos)
                if codigoEliminar:
                    dao.eliminarCurso(codigoEliminar)
                    print("Curso eliminado correctamente...")
                    print("************************************")
                    print("\n") 
                    menuPrincipal()
                else:
                    print("No hay cursos registrados...")                
        except Exception as e:
            print("Error al eliminar el curso: ", e)
    else:
        print("Opcion no valida...")

menuPrincipal()