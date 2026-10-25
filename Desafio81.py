class Nodo:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.izq = None
        self.der = None


# Crear el árbol
raiz = Nodo(12, ["Ana", "Luis"])
raiz.izq = Nodo(11, ["Sofía", "Pedro"])
raiz.der = Nodo(10, ["Juan", "María"])

raiz.izq.izq = Nodo(9, ["Carlos", "Lucía"])
raiz.izq.der = Nodo(8, ["Martín", "Laura"])

raiz.der.izq = Nodo(7, ["Diego", "Paula"])
raiz.der.der = Nodo(6, ["Valentina", "Mateo"])


def recorrido_por_niveles(raiz):
    cola = [raiz]

    while cola:
        nodo = cola.pop(0)

        print("Grado:", nodo.grado)
        print("Estudiantes:", nodo.estudiantes)

        if nodo.izq:
            cola.append(nodo.izq)

        if nodo.der:
            cola.append(nodo.der)


recorrido_por_niveles(raiz)