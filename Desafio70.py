import math


class NegativeNumberError(Exception):
    pass


try:
    numero = float(input("Ingrese un número: "))

    if numero < 0:
        raise NegativeNumberError("No se puede calcular la raíz de un número negativo.")

    resultado = math.sqrt(numero)

    print("La raíz cuadrada es:", resultado)

except NegativeNumberError as error:
    print("Error:", error)

except ValueError:
    print("Error: debe ingresar un número válido.")