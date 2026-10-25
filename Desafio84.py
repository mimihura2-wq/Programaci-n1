estudiantes = [
    ["Ana", 7.5],
    ["Bruno", 9.2],
    ["Carlos", 6.8],
    ["Diana", 8.5],
    ["Elena", 9.7]
]


def ordenamiento_seleccion(estudiantes):
    for i in range(len(estudiantes)):
        mayor = i

        for j in range(i + 1, len(estudiantes)):
            if estudiantes[j][1] > estudiantes[mayor][1]:
                mayor = j

        estudiantes[i], estudiantes[mayor] = estudiantes[mayor], estudiantes[i]


ordenamiento_seleccion(estudiantes)

print("Estudiantes ordenados por promedio:")

for estudiante in estudiantes:
    print(estudiante[0], "-", estudiante[1])