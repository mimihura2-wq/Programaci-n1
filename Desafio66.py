#Polimorfismo en operaciones matemáticas
class Operacion:
    def resultado(self, numero1, numero2):
        pass


class Suma(Operacion):
    def resultado(self, numero1, numero2):
        return numero1 + numero2


class Multiplicacion(Operacion):
    def resultado(self, numero1, numero2):
        return numero1 * numero2


# Crear objetos
suma = Suma()
multiplicacion = Multiplicacion()

# Guardar las operaciones en una misma lista
operaciones = [suma, multiplicacion]

# Realizar las operaciones
for operacion in operaciones:
    print("Resultado:", operacion.resultado(5, 3))