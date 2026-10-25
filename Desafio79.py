class Nodo:
    def __init__(self, valor):
        self.val = valor
        self.izq = None
        self.der = None


def insertar(raiz, valor):

    if raiz is None:
        return Nodo(valor)

    if valor < raiz.val:
        raiz.izq = insertar(raiz.izq, valor)

    elif valor > raiz.val:
        raiz.der = insertar(raiz.der, valor)

    return raiz


def buscar(raiz, valor):

    if raiz is None:
        return False

    if raiz.val == valor:
        return True

    if valor < raiz.val:
        return buscar(raiz.izq, valor)

    return buscar(raiz.der, valor)


# Crear el árbol
valores = [8, 3, 10, 1, 6, 14, 4]

raiz = None

for valor in valores:
    raiz = insertar(raiz, valor)


# Buscar un número
numero = int(input("Ingrese el número que desea buscar: "))

if buscar(raiz, numero):
    print("El número existe en el árbol.")
else:
    print("El número no existe en el árbol.")