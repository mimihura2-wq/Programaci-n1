# Crear el inventario de la cadena de tiendas

tiendas = {
    "Tienda Centro": {
        "productos": [
            {"nombre": "Laptop", "cantidad": 5, "precio": 35000},
            {"nombre": "Mouse", "cantidad": 20, "precio": 800},
            {"nombre": "Teclado", "cantidad": 10, "precio": 1500}
        ],
        "empleados": [
            "Ana",
            "Carlos"
        ],
        "transacciones": [
            {"producto": "Mouse", "cantidad": 2, "tipo": "Venta"},
            {"producto": "Laptop", "cantidad": 1, "tipo": "Venta"}
        ]
    },

    "Tienda Norte": {
        "productos": [
            {"nombre": "Monitor", "cantidad": 8, "precio": 12000},
            {"nombre": "Teclado", "cantidad": 15, "precio": 1500}
        ],
        "empleados": [
            "Lucía",
            "Pedro"
        ],
        "transacciones": [
            {"producto": "Monitor", "cantidad": 1, "tipo": "Venta"},
            {"producto": "Teclado", "cantidad": 3, "tipo": "Venta"}
        ]
    }
}


# Mostrar la información de las tiendas

for nombre_tienda, datos in tiendas.items():

    print("\nTienda:", nombre_tienda)

    print("Productos:")
    for producto in datos["productos"]:
        print(
            "-",
            producto["nombre"],
            "| Cantidad:",
            producto["cantidad"],
            "| Precio:",
            producto["precio"]
        )

    print("Empleados:")
    for empleado in datos["empleados"]:
        print("-", empleado)

    print("Transacciones:")
    for transaccion in datos["transacciones"]:
        print(
            "-",
            transaccion["tipo"],
            "| Producto:",
            transaccion["producto"],
            "| Cantidad:",
            transaccion["cantidad"]
        )