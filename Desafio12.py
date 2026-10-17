# Solicitar texto al usuario
texto = input("Ingrese un texto: ").strip()
# Validar que no esté vacío
while texto == "":
print("Debe ingresar un texto válido.")
texto = input("Ingrese un texto: ").strip()
# Reemplazar saltos de línea por espacios
texto = texto.replace("\n", " ")
# Separar palabras correctamente
palabras = texto.split()
# Contar palabras
cantidad_palabras = len(palabras)
# Mostrar resultado final
print("\n========== RESULTADO ==========")
print(f"Texto ingresado: {texto}")
print(f"Cantidad de palabras: {cantidad_palabras}")
print(“Operación realizada correctamente.”)