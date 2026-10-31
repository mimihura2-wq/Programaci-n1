registros = [
    ("Montevideo", 22, 70),
    ("Salto", 30, 60),
    ("Colonia", 24, 75),
    ("Punta del Este", 20, 80),
    ("Paysandú", 28, 65)
]


# Ciudad con mayor temperatura
mayor_temperatura = registros[0]

for registro in registros:
    if registro[1] > mayor_temperatura[1]:
        mayor_temperatura = registro

print("Ciudad con mayor temperatura:")
print(mayor_temperatura[0], "-", mayor_temperatura[1], "°C")


# Ciudad con menor temperatura
menor_temperatura = registros[0]

for registro in registros:
    if registro[1] < menor_temperatura[1]:
        menor_temperatura = registro

print("\nCiudad con menor temperatura:")
print(menor_temperatura[0], "-", menor_temperatura[1], "°C")


# Promedio general de humedad
total_humedad = 0

for registro in registros:
    total_humedad += registro[2]

promedio_humedad = total_humedad / len(registros)

print("\nPromedio de humedad:", promedio_humedad, "%")