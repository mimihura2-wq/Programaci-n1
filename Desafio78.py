class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor


raiz = Nodo(10)

raiz.izq = Nodo(5)
raiz.der = Nodo(15)

raiz.izq.izq = Nodo(3)
raiz.izq.der = Nodo(8)

raiz.der.izq = Nodo(12)
raiz.der.der = Nodo(20)


def maximo_postorder(raiz):
    if raiz is None:
        return None

    maximo_izquierda = maximo_postorder(raiz.izq)
    maximo_derecha = maximo_postorder(raiz.der)

    maximo = raiz.val

    if maximo_izquierda is not None and maximo_izquierda > maximo:
        maximo = maximo_izquierda

    if maximo_derecha is not None and maximo_derecha > maximo:
        maximo = maximo_derecha

    return maximo


resultado = maximo_postorder(raiz)

print("El valor máximo es:", resultado)