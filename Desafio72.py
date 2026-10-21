codigos = ["A123", "B456", "C789", "D321", "E654"]

codigo = input("Ingrese el código del producto: ")

if codigo in codigos:
    posicion = codigos.index(codigo)
    print("Código encontrado.")
    print("Posición:", posicion)

else:
    print("El código no fue encontrado.")