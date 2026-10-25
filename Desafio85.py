class Nodo:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        self.izq = None
        self.der = None


def insertar(raiz, nombre, promedio):
    if raiz is None:
        return Nodo(nombre, promedio)

    if promedio < raiz.promedio:
        raiz.izq = insertar(raiz.izq, nombre, promedio)
    else:
        raiz.der = insertar(raiz.der, nombre, promedio)

    return raiz


def inorden(raiz):
    if raiz:
        inorden(raiz.izq)
        print(raiz.nombre, "-", raiz.promedio)
        inorden(raiz.der)


estudiantes = [
    ["Ana", 7.5],
    ["Bruno", 9.2],
    ["Carlos", 6.8],
    ["Diana", 8.5],
    ["Elena", 9.7]
]

raiz = None

for estudiante in estudiantes:
    nombre = estudiante[0]
    promedio = estudiante[1]
    raiz = insertar(raiz, nombre, promedio)

print("Estudiantes ordenados por promedio:")
inorden(raiz)