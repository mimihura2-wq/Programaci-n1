import csv

nombre_libro = input("Ingrese el nombre del libro: ")
nueva_cantidad = int(input("Ingrese la nueva cantidad de copias: "))

libros = []

with open("inventario.csv", "r") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        if fila[0] == nombre_libro:
            fila[1] = str(nueva_cantidad)

        libros.append(fila)


with open("inventario.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    for fila in libros:
        escritor.writerow(fila)

print("Inventario actualizado correctamente.")