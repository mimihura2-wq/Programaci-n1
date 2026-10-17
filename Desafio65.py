import math


class Figura:
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Crear objetos
circulo = Circulo(5)
cuadrado = Cuadrado(4)

# Guardar ambos objetos en una misma lista
figuras = [circulo, cuadrado]

# Recorrer la lista y calcular las áreas
for figura in figuras:
    print(f"{type(figura).__name__}: área = {figura.area():.2f}")
