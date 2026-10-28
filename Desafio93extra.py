eventos = [
    ("10:00", "Ana", "inicio_sesion"),
    ("10:05", "Juan", "inicio_sesion"),
    ("10:10", "Ana", "compra"),
    ("10:15", "Pedro", "inicio_sesion"),
    ("10:20", "Ana", "cerrar_sesion"),
    ("10:25", "Juan", "compra")
]

usuario = input("Ingrese el usuario: ")

print("Eventos del usuario:")

for evento in eventos:
    if evento[1] == usuario:
        print(evento)


acciones = {}

for evento in eventos:
    accion = evento[2]

    if accion in acciones:
        acciones[accion] += 1
    else:
        acciones[accion] = 1

print("Cantidad de veces que aparece cada acción:")
print(acciones)