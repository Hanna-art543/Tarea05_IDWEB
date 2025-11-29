def agregar_estudiantes():
    estudiantes = {}
    numEstudiantes = int(input("Ingrese el número de estudiantes: "))

    for i in range(numEstudiantes):
        nombre = input("Nombre del estudiante: ")
        nota = float(input("Nota (0-20): "))
        estudiantes[nombre] = nota
    
    return estudiantes


def mostrar_estudiantes(estudiantes):
    print("\nLISTA DE ESTUDIANTES")
    for clave, valor in estudiantes.items():
        print(f"{clave}: {valor}")


def nota_alta(estudiantes):
    mayor_nota = -1
    mejor_estudiante = ""

    for nombre, nota in estudiantes.items():
        if nota > mayor_nota:
            mayor_nota = nota
            mejor_estudiante = nombre

    return mejor_estudiante, mayor_nota


def promedio_notas(estudiantes):
    suma = sum(estudiantes.values())
    numEstudiantes = len(estudiantes)
    return suma / numEstudiantes


def main():
    estudiantes = agregar_estudiantes()
    mostrar_estudiantes(estudiantes)

    nombre, nota = nota_alta(estudiantes)
    print(f"\nEstudiante con la nota más alta: {nombre} - {nota}")

    promedio = promedio_notas(estudiantes)
    print(f"Promedio de todas las notas: {promedio:.2f}")


main()
