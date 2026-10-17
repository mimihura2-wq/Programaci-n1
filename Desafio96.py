inventario = {
    "P001": {
        "nombre": "Teclado",
        "precio": 1200,
        "stock": 10
    },
    "P002": {
        "nombre": "Mouse",
        "precio": 800,
        "stock": 15
    }
}


# Agregar un producto
inventario["P003"] = {
    "nombre": "Monitor",
    "precio": 7500,
    "stock": 5
}


# Actualizar el stock de un producto
inventario["P001"]["stock"] += 5


# Buscar un producto por código
codigo = input("Ingrese el código del producto: ")

if codigo in inventario:
    producto = inventario[codigo]

    print("Nombre:", producto["nombre"])
    print("Precio:", producto["precio"])
    print("Stock:", producto["stock"])
else:
    print("Producto no encontrado")