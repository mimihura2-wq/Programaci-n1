lista1 = [1, 2, 3, 4]
lista2 = [10, 20]

resultado = []

cantidad = max(len(lista1), len(lista2))

for i in range(cantidad):

    numero1 = lista1[i] if i < len(lista1) else 0
    numero2 = lista2[i] if i < len(lista2) else 0

    resultado.append(numero1 + numero2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Resultado:", resultado)