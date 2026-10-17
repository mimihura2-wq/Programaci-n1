import numpy as np

# Crear tablero de 5x5 lleno de ceros
tablero = np.zeros((5, 5), dtype=int)

# Colocar 3 barcos en posiciones aleatorias
barcos_colocados = 0

while barcos_colocados < 3:
    fila = np.random.randint(0, 5)
    columna = np.random.randint(0, 5)

    # Verificar que no haya ya un barco en esa posición
    if tablero[fila, columna] == 0:
        tablero[fila, columna] = 1
        barcos_colocados += 1

# Función para verificar un disparo
def disparar(x, y):
    if tablero[x, y] == 1:
        print("¡BooooM! Golpeaste un barco.")
    else:
        print("Agua. No hay ningún barco en esa posición.")

# Mostrar el tablero para comprobar
print(tablero)

# Ejemplo de disparo
disparar(2, 3)
