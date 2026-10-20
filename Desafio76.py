class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor


# Crear el árbol
raiz = Nodo(1)

raiz.izq = Nodo(2)
raiz.der = Nodo(3)

raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)


# Recorrido en preorden
def print_preorder(raiz):
    if raiz:
        print(raiz.val, end=" ")
        print_preorder(raiz.izq)
        print_preorder(raiz.der)


print_preorder(raiz)