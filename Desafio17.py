import random

# Lista de autos
autos = ["ROJO", "AZUL", "VERDE", "NEGRO"]

# Diccionario para velocidad y distancia
velocidades = {}
distancias = {}

# Inicio de velocidades aleatorias y distancias
for auto in autos:
    velocidades[auto] = random.randint(10, 20)  # km/h ficticios
    distancias[auto] = 0

print("Inicio de la carrera\n")

# Simulación de 10 segundos
for segundo in range(1, 11):
    print(f"Segundo {segundo}")

    for auto in autos:
        # Cada auto avanza según su velocidad
        distancias[auto] += velocidades[auto]

        print(
            f"Auto {auto} | "
            f"Velocidad: {velocidades[auto]} | "
            f"Distancia: {distancias[auto]}"
        )

    
# Buscar la mayor distancia recorrida
max_distancia = max(distancias.values())

# Buscar ganadores (por si hay empate)
ganadores = []

for auto, distancia in distancias.items():
    if distancia == max_distancia:
        ganadores.append(auto)

# Mostrar resultado final
print("\n Resultado final")

if len(ganadores) == 1:
    print(f"El ganador es el auto {ganadores[0]} \nGAME OVER")
else:
    print("Hubo un empate entre los autos:")
    for ganador in ganadores:
        print(f" {ganador}")
