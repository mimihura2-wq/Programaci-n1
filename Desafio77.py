class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor


raiz = Nodo(1)

raiz.izq = Nodo(2)
raiz.der = Nodo(3)

raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)


def suma_inorder(raiz):
    if raiz is None:
        return 0

    suma_izquierda = suma_inorder(raiz.izq)
    suma_derecha = suma_inorder(raiz.der)

    return suma_izquierda + raiz.val + suma_derecha


resultado = suma_inorder(raiz)

print("La suma es:", resultado)