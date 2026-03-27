"""
Menú principal que permite interactuar con la API REST desarrollada con FastAPI.
A través de este menú se pueden gestionar las entidades del sistema:

- Profesores
- Estudiantes
- Materias
- Periodos
- Grados
- Notas

El menú utiliza funciones del CRUD implementadas con httpx
para consumir los endpoints de la API.
"""

# Importación de funciones CRUD para cada entidad
# Estas funciones se encargan de consumir la API FastAPI
# mediante peticiones HTTP utilizando la librería httpx.

from src.crud.estudiante_crud import (
    actualizar_estudiante,
    crear_estudiante,
    eliminar_estudiante,
    obtener_estudiantes,
)

from src.crud.grado_crud import (
    actualizar_grado,
    crear_grado,
    eliminar_grado,
    obtener_grados,
)

from src.crud.materia_crud import (
    actualizar_materia,
    crear_materia,
    eliminar_materia,
    obtener_materias,
)

from src.crud.nota_crud import (
    actualizar_nota,
    crear_nota,
    eliminar_nota,
    obtener_notas,
)

from src.crud.periodo_crud import (
    actualizar_periodo,
    crear_periodo,
    eliminar_periodo,
    obtener_periodos,
)

from src.crud.profesor_crud import (
    actualizar_profesor,
    crear_profesor,
    eliminar_profesor,
    obtener_profesores,
)


def menu_principal():
    """
    Menú principal del sistema.

    Permite al usuario seleccionar qué entidad desea gestionar.
    Cada opción redirige a un submenú específico para realizar
    operaciones del CRUD sobre la entidad seleccionada.
    """

    while True:
        print("\n===== SISTEMA DE ESCUELA =====")
        print("1. Gestionar Profesores")
        print("2. Gestionar Estudiantes")
        print("3. Gestionar Materias")
        print("4. Gestionar Periodos")
        print("5. Gestionar Grados")
        print("6. Gestionar Notas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        # Redirección a los submenús según la opción elegida
        if opcion == "1":
            menu_profesores()
        elif opcion == "2":
            menu_estudiantes()
        elif opcion == "3":
            menu_materias()
        elif opcion == "4":
            menu_periodos()
        elif opcion == "5":
            menu_grados()
        elif opcion == "6":
            menu_notas()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida")


def menu_profesores():
    """
    Submenú para la gestión de profesores.

    Permite listar, crear, actualizar o eliminar profesores
    utilizando las funciones del CRUD que consumen la API.
    """

    while True:
        print("\n--- PROFESORES ---")
        print("1. Ver profesores")
        print("2. Crear profesor")
        print("3. Actualizar profesor")
        print("4. Eliminar profesor")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Obtener y mostrar todos los profesores
            print(obtener_profesores())

        elif opcion == "2":
            # Solicitar datos para crear un nuevo profesor
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            especialidad = input("Especialidad: ")
            telefono = input("Telefono: ")

            print(crear_profesor(nombre, apellido, correo, especialidad, telefono))

        elif opcion == "3":
            # Actualizar información de un profesor existente
            id_profesor = int(input("ID del profesor: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            especialidad = input("Especialidad: ")
            telefono = input("Telefono: ")

            print(
                actualizar_profesor(
                    id_profesor, nombre, apellido, correo, especialidad, telefono
                )
            )

        elif opcion == "4":
            # Eliminar un profesor por su ID
            id_profesor = int(input("ID del profesor: "))
            print(eliminar_profesor(id_profesor))

        elif opcion == "5":
            break

        else:
            print("Opción no válida")


def menu_estudiantes():
    """
    Submenú para la gestión de estudiantes.
    """

    while True:
        print("\n--- ESTUDIANTES ---")
        print("1. Ver estudiantes")
        print("2. Crear estudiante")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(obtener_estudiantes())

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            id_grado = int(input("ID del grado: "))

            print(crear_estudiante(nombre, apellido, correo, id_grado))

        elif opcion == "3":
            id_estudiante = int(input("ID del estudiante: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            id_grado = int(input("ID del grado: "))

            print(
                actualizar_estudiante(id_estudiante, nombre, apellido, correo, id_grado)
            )

        elif opcion == "4":
            id_estudiante = int(input("ID del estudiante: "))
            print(eliminar_estudiante(id_estudiante))

        elif opcion == "5":
            break

        else:
            print("Opción no válida")


def menu_materias():
    """
    Submenú para la gestión de materias.
    """

    while True:
        print("\n--- MATERIAS ---")
        print("1. Ver materias")
        print("2. Crear materia")
        print("3. Actualizar materia")
        print("4. Eliminar materia")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(obtener_materias())

        elif opcion == "2":
            nombre = input("Nombre: ")
            id_profesor = int(input("ID del profesor: "))

            print(crear_materia(nombre, id_profesor))

        elif opcion == "3":
            id_materia = int(input("ID de la materia: "))
            nombre = input("Nombre: ")
            id_profesor = int(input("ID del profesor: "))

            print(actualizar_materia(id_materia, nombre, id_profesor))

        elif opcion == "4":
            id_materia = int(input("ID de la materia: "))
            print(eliminar_materia(id_materia))

        elif opcion == "5":
            break

        else:
            print("Opción no válida")


def menu_periodos():
    """
    Submenú para la gestión de periodos académicos.
    """

    while True:
        print("\n--- PERIODOS ---")
        print("1. Ver periodos")
        print("2. Crear periodo")
        print("3. Actualizar periodo")
        print("4. Eliminar periodo")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(obtener_periodos())

        elif opcion == "2":
            nombre = input("Nombre: ")
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")

            print(crear_periodo(nombre, fecha_inicio, fecha_fin))

        elif opcion == "3":
            id_periodo = int(input("ID del periodo: "))
            nombre = input("Nombre: ")
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")

            print(actualizar_periodo(id_periodo, nombre, fecha_inicio, fecha_fin))

        elif opcion == "4":
            id_periodo = int(input("ID del periodo: "))
            print(eliminar_periodo(id_periodo))

        elif opcion == "5":
            break

        else:
            print("Opción no válida")


def menu_grados():
    """
    Submenú para la gestión de grados académicos.
    """

    while True:
        print("\n--- GRADOS ---")
        print("1. Ver grados")
        print("2. Crear grado")
        print("3. Actualizar grado")
        print("4. Eliminar grado")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(obtener_grados())

        elif opcion == "2":
            nombre = input("Nombre del grado: ")
            print(crear_grado(nombre))

        elif opcion == "3":
            id_grado = int(input("ID del grado: "))
            nombre = input("Nombre del grado: ")

            print(actualizar_grado(id_grado, nombre))

        elif opcion == "4":
            id_grado = int(input("ID del grado: "))
            print(eliminar_grado(id_grado))

        elif opcion == "5":
            break

        else:
            print("Opción no válida")


def menu_notas():
    """
    Submenú para la gestión de notas académicas.
    """

    while True:
        print("\n--- NOTAS ---")
        print("1. Ver notas")
        print("2. Crear nota")
        print("3. Actualizar nota")
        print("4. Eliminar nota")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(obtener_notas())

        elif opcion == "2":
            clasificacion = float(input("Clasificación: "))
            id_estudiante = int(input("ID del estudiante: "))
            id_profesor = int(input("ID del profesor: "))
            id_materia = int(input("ID de la materia: "))
            id_periodo = int(input("ID del periodo: "))

            print(
                crear_nota(
                    clasificacion, id_estudiante, id_profesor, id_materia, id_periodo
                )
            )

        elif opcion == "3":
            id_nota = int(input("ID de la nota: "))
            clasificacion = float(input("Clasificación: "))
            id_estudiante = int(input("ID del estudiante: "))
            id_profesor = int(input("ID del profesor: "))
            id_materia = int(input("ID de la materia: "))
            id_periodo = int(input("ID del periodo: "))

            print(
                actualizar_nota(
                    id_nota,
                    clasificacion,
                    id_estudiante,
                    id_profesor,
                    id_materia,
                    id_periodo,
                )
            )

        elif opcion == "4":
            id_nota = int(input("ID de la nota: "))
            print(eliminar_nota(id_nota))

        elif opcion == "5":
            break

        else:
            print("Opción no válida")


# Punto de entrada del programa
# Este bloque permite ejecutar el menú principal
# cuando el archivo se ejecuta directamente.

if __name__ == "__main__":
    menu_principal()
