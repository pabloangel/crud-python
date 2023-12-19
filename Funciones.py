def listarCursos(cursos):
    print("Cursos: ")
    print("************************************************************************")
    contador=1
    for cur in cursos:
        datos="{0}. Codigo: {1}, - Nombre: {2},  Creditos: {3}"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
        
def pedirDatosRegistro():
    codigoCorrecto = False
    while not codigoCorrecto:
        codigo = input("Ingrese el codigo del curso: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("El codigo debe tener 6 caracteres...")

    nombre = input("Ingrese el nombre del curso: ")

    creditosCorrecto = False
    while not creditosCorrecto:
        creditos = input("Ingrese el numero de creditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):                
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("El numero de creditos debe ser mayor a cero...")
        else:
            print(creditos  + " no es un numero. Favor intentar nuevamente...")
    
    
    curso = (codigo, nombre, creditos)
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    curso = None  # Valor por defecto
    while not existeCodigo:
        codigoEditar = input(" Ingrese el codigo del curso a editar: ")
        try:
            codigoEditar = int(codigoEditar)  # Convertir a entero
        except ValueError:
            print("El código ingresado no es un número. Por favor, intente de nuevo.")
            continue
        for cur in cursos:
            if cur[0] == codigoEditar:  # Ahora la comparación es entre enteros
                existeCodigo = True
                break
        if not existeCodigo:
            print("El código ingresado no existe. Por favor, intente de nuevo.")
    nombre = input("Ingrese el nombre del curso a modificar: ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese el numero de creditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):                
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("El numero de creditos debe ser mayor a cero...")
        else:
            print(creditos  + " no es un numero. Favor intentar nuevamente...")

    curso = (codigoEditar, nombre, creditos)

    return curso
 
def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    while not existeCodigo:
        codigoEliminar = input("Ingrese el codigo del curso a eliminar: ")
        try:
            codigoEliminar = int(codigoEliminar)
        except ValueError:
            print("El código ingresado no es un número. Por favor, intente de nuevo.")
            continue
        for cur in cursos:
            if cur[0] == codigoEliminar:
                existeCodigo = True
                break
        if not existeCodigo:
            print("El código ingresado no existe. Por favor, intente de nuevo.")
    return codigoEliminar
    