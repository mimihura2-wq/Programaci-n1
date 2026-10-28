ventas = [
    ("P001", 5, 100),
    ("P002", 3, 250),
    ("P001", 2, 100),
    ("P003", 8, 50),
    ("P002", 4, 250)
]

# Calcular el total de ingresos
total_ingresos = 0

for venta in ventas:
    producto = venta[0]
    cantidad = venta[1]
    precio = venta[2]

    total_ingresos += cantidad * precio

print("Total de ingresos:", total_ingresos)


# Buscar el producto más vendido
cantidades = {}

for venta in ventas:
    producto = venta[0]
    cantidad = venta[1]

    if producto in cantidades:
        cantidades[producto] += cantidad
    else:
        cantidades[producto] = cantidad

producto_mas_vendido = max(cantidades, key=cantidades.get)

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad vendida:", cantidades[producto_mas_vendido])