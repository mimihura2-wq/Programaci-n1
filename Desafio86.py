libro = input("Ingrese el nombre del libro: ")
prestatario = input("Ingrese el nombre del prestatario: ")
fecha = input("Ingrese la fecha del préstamo: ")

with open("prestamos.txt", "a") as archivo:
    archivo.write("Libro: " + libro + "\n")
    archivo.write("Prestatario: " + prestatario + "\n")
    archivo.write("Fecha: " + fecha + "\n")
    archivo.write("\n")

print("Préstamo registrado correctamente.")