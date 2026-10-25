class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def construir_arbol():
    raiz = Nodo("+")
    
    raiz.izq = Nodo(5)
    
    raiz.der = Nodo("*")
    raiz.der.izq = Nodo(3)
    raiz.der.der = Nodo(4)
    
    return raiz


def evaluar(raiz):

    if raiz.izq is None and raiz.der is None:
        return raiz.valor

    izquierda = evaluar(raiz.izq)
    derecha = evaluar(raiz.der)

    if raiz.valor == "+":
        return izquierda + derecha

    elif raiz.valor == "-":
        return izquierda - derecha

    elif raiz.valor == "*":
        return izquierda * derecha

    elif raiz.valor == "/":
        return izquierda / derecha


arbol = construir_arbol()

resultado = evaluar(arbol)

print("Resultado:", resultado)