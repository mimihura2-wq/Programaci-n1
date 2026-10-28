with open("prestamos.txt", "r") as archivo:
    prestamos = archivo.read().strip().split("\n\n")


print("Préstamos actuales:")

for i in range(len(prestamos)):
    print(i + 1, "-", prestamos[i].replace("\n", " | "))


numero = int(input("Ingrese el número del préstamo que desea eliminar: "))

if numero >= 1 and numero <= len(prestamos):
    prestamos.pop(numero - 1)

    with open("prestamos.txt", "w") as archivo:
        for prestamo in prestamos:
            archivo.write(prestamo + "\n\n")

    print("Préstamo eliminado correctamente.")
else:
    print("Número de préstamo inválido.")