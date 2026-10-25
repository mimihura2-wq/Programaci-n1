calificaciones = [
    [8, 7, 9],
    [6, 10, 8],
    [9, 8, 7]
]

calificacion_buscar = int(input("Ingrese la calificación que desea buscar: "))

def buscar_calificacion(calificaciones, calificacion_buscar):
    for estudiante in range(len(calificaciones)):
        for materia in range(len(calificaciones[estudiante])):
            if calificaciones[estudiante][materia] == calificacion_buscar:
                return estudiante, materia

    return -1, -1


estudiante, materia = buscar_calificacion(calificaciones, calificacion_buscar)

if estudiante != -1:
    print("Calificación encontrada.")
    print("Estudiante:", estudiante + 1)
    print("Materia:", materia + 1)
else:
    print("La calificación no fue encontrada.")