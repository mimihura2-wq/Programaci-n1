texto = input("Ingrese un texto: ").strip()

while texto == "":
    print("Debe ingresar un texto válido.")
    texto = input("Ingrese un texto: ").strip()

texto = texto.replace("\n", " ")

palabras = texto.split()

cantidad_palabras = len(palabras)

print("\n========== RESULTADO ==========")
print(f"Texto ingresado: {texto}")
print(f"Cantidad de palabras: {cantidad_palabras}")
print("Operación realizada correctamente.")