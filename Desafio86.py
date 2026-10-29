# Solicitar los datos del préstamo
libro = input("Nombre del libro: ")
prestatario = input("Nombre del prestatario: ")
fecha = input("Fecha del préstamo: ")

# Guardar el préstamo en el archivo
with open("prestamos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"Libro: {libro}, Prestatario: {prestatario}, Fecha: {fecha}\n")

print("Préstamo registrado correctamente.")