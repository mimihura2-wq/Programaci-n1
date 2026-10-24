estudiantes = ["Ana", "Bruno", "Carlos", "Diego", "Elena", "Florencia", "Gabriel"]

def busqueda_binaria(estudiantes, nombre_buscar):
    bajo = 0
    alto = len(estudiantes) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2

        if estudiantes[medio] == nombre_buscar:
            return medio
        elif estudiantes[medio] < nombre_buscar:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1


nombre = input("Ingrese el nombre del estudiante que desea buscar: ")

resultado = busqueda_binaria(estudiantes, nombre)

if resultado != -1:
    print("Estudiante encontrado en la posición:", resultado)
else:
    print("El estudiante no se encuentra en la lista.")